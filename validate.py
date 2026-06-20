import json
from schema import SCHEMA as schema, VERSION
import re

def validate(book):
    
    # get all schema keys
    schema_keys = schema.keys()

    # get all keys in the book
    book_keys = book.keys()

    # get required keys
    required_keys = []
    for key in schema_keys:
        if schema[key]["required"] == True:
            required_keys.append(key)

    # flag for schema validation
    has_valid_schema = True

    # check book keys
    r_keys = 0
    for key in list(book):
        if key not in schema_keys:
            print(f"NOK: invalid key found: {key}")
            return False

    # check required keys
    for key in required_keys:    
        if key not in book:
            has_valid_schema = False
            print(f"> Required key [{key}] not found!")
            print(f">> VALIDATION FAIL")
            

    for key in book_keys:
        # if a key has  "allowed_values"
        # check that the value of the key is valid
        if "allowed_values" in schema[key] and book[key] not in schema[key]["allowed_values"]:
            has_valid_schema = False
            print(f"> found {key}:({book[key]})  with allowed values : {schema[key]['allowed_values']}")
            print(f">> VALIDATION FAIL")            
        # if a key has "allowed_patterns"
        # check that the value of the key follows the pattern
        if "allowed_patterns" in schema[key]:
            # check book entry against the allowed patterns
            has_valid_pattern = False
            for pattern in schema[key]['allowed_patterns']:
                has_valid_pattern = has_valid_pattern or bool(re.match(pattern, book[key]))
            if not has_valid_pattern:
                has_valid_schema = False
                print(f"> found {key}:({book[key]}) with expected patterns: {schema[key]['allowed_patterns']}")
                print(f">> VALIDATION FAIL")
        # if a key has minmax
        # check that the book entry has valid values
        if "min" in schema[key]:
            if book[key] < schema[key]['min']:
                has_valid_schema = False
                print(f"> found {key}:({book[key]}) with expected min: {schema[key]['min']}")
                print(f">> VALIDATION FAIL")
        if "max" in schema[key]:
            if book[key] > schema[key]['max']:
                has_valid_schema = False
                print(f"> found {key}:({book[key]}) with expected max: {schema[key]['max']}")
                print(f">> VALIDATION FAIL")

    print(f"{'Unknown' if 'title' not in book.keys() else book['title']} validation pass : {has_valid_schema}")
    return has_valid_schema


books = [
    {"title": "Dune", "status": "read", "last_read": "2021", "author": "Frank Herbert", "rating": 10, "format": "physical"},
    {"title": "1984", "status": "reading", "last_read": "2024-03", "author": "George Orwell"},
    {"title": "Sapiens", "status": "abandoned", "last_read": "20211", "author": "Yuval Noah Harari"},
    {"title": "Neuromancer", "status": "not started"},
    {"title": "The Hobbit", "status": "done", "last_read": "2022-5", "author": "Tolkien"},
    {"title": "Atomic Habits", "status": "read", "last_read": "", "author": "James Clear"},
    {"title": "Shogun", "status": "read", "last_read": "banana", "author": "James Clavell"},
    {"title": "Book with missing status"},
    {"status": "read"}
]

for book in books:
    validate(book)