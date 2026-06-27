from sys import argv
import crud
from schema import SCHEMA as schema

def add_book():
    entries = schema.keys()
    book = {}
    for entry in entries:
        question = f"Enter {entry}"
        question += "*" if schema[entry].get("required") else ""
        question += " (" + " | ".join(schema[entry].get("allowed_patterns")) + ")" if schema[entry].get("allowed_patterns") else ""
        question += " (" + " | ".join(schema[entry].get("allowed_values")) + ")" if schema[entry].get("allowed_values") else ""
        value = input(question + "\n: ")
        if value != "":
            book[entry] = value
    crud.create(book)

if len(argv) < 2:
    print("No arguments passed, nothing to do")

if len(argv) >= 3:
    match argv[2]:
        case "-t":
            print("Using test db")
            crud.BOOKS_FILE = "books_test.json"
        case _:
            pass

if len(argv) >= 2:
    match argv[1]:
        case "add":
            add_book()
        case "list":
            print("Listing")
        case _:
            print("Invalid option!")

