from sys import argv
import crud
from schema import SCHEMA as schema

def add_book():
    entries = schema.keys()
    book = {}
    for entry in entries:
    
        # build the input question
        question = f"Enter {entry}, expected format is '{schema[entry]['type'].__name__}' "
        
        # is the entry a required field?
        if schema[entry].get("required"):
            question += "(required)"

        # does the entry have allowed patterns in the schema?
        if schema[entry].get("allowed_patterns"):
            question += f" ({' / '.join(schema[entry].get('allowed_patterns'))})"

        # does the entry have allowed values in the schema?
        if schema[entry].get("allowed_values"):
            question += f" ({' / '.join(schema[entry].get('allowed_values'))})"

        # does the entry have a minimum value in the schema?
        if schema[entry].get("min"):
            question += f" (min: {schema[entry].get('min')})"
        
        # does the entry have a maximum value in the schema?
        if schema[entry].get("max"):
            question += f" (max: {schema[entry].get('max')})"
        
        # does the entry expect a list from the user?
        if schema[entry].get("type") == list:
            question += f" (comma-separated list)"

        # get value from user
        value = input(question + "\n: ")


        if schema[entry]["type"] == list:
            value = [x.strip() for x in value.split(",") if x.strip() != ""]
            if len(value) > 0:
                book[entry] = value
        
        elif schema[entry]["type"] == int and value != "":
            book[entry] = int(value)
        
        else:
            if len(value) > 0:
                book[entry] = value
    
    
    crud.create(book)


def list_books():
    # read from the database and list books
    books = crud.load_books()
    column_length = 25
    required_keys = [x for x in schema.keys() if schema[x].get("required")]
    required_keys_padded = [x.ljust(column_length," ") for x in required_keys]
    print("".join(required_keys_padded))
    print("-"*(2*column_length + 3))
    for book in books:
        row = ""
        for key in required_keys:
            row += book[key].ljust(column_length)
        print(row)    

    

if len(argv) < 2:
    print("No arguments passed, nothing to do")

if len(argv) >= 3:
    match argv[2]:
        case "-t":
            print("---- Using test db: books_test.json ----")
            crud.BOOKS_FILE = "books_test.json"
        case _:
            pass

if len(argv) >= 2:
    match argv[1]:
        case "add":
            add_book()
        case "list":
            list_books()
        case _:
            print("Invalid option!")

