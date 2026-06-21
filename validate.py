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
            print(f"> NOK: invalid key found: {key}")
            return False


    # check required keys
    for key in required_keys:    
        if key not in book:
            has_valid_schema = False
            print(f"> Required key [{key}] not found!")
    
    # the book has valid and required keys. 
    # now let's check if it has the right kind of keys
    for key in book_keys:
        if type(book[key]) is not schema[key]['type']:
            has_valid_schema = False
            print(f"> {key} is expected to be of type {schema[key]['type']}, but is {type(book[key])}")
        else:
            # if a key has  "allowed_values"
            # check that the value of the key is valid
            if "allowed_values" in schema[key] and book[key] not in schema[key]["allowed_values"]:
                has_valid_schema = False
                print(f">{key} has value \"{book[key]}\" but allowed values are {schema[key]['allowed_values']}")
            # if a key has "allowed_patterns"
            # check that the value of the key follows the pattern
            if "allowed_patterns" in schema[key]:
                # check book entry against the allowed patterns
                has_valid_pattern = False
                for pattern in schema[key]['allowed_patterns']:
                    has_valid_pattern = has_valid_pattern or bool(re.match(pattern, book[key]))
                if not has_valid_pattern:
                    has_valid_schema = False
                    print(f"> {key} has value ({book[key]}) but expected patterns are {schema[key]['allowed_patterns']}")
            # if a key has minmax
            # check that the book entry has valid values
            if "min" in schema[key]:
                if book[key] < schema[key]['min']:
                    has_valid_schema = False
                    print(f"> {key} has value ({book[key]}) but allowed min value is {schema[key]['min']}")
            if "max" in schema[key]:
                if book[key] > schema[key]['max']:
                    has_valid_schema = False
                    print(f"> {key} has value ({book[key]}) but allowed max value is {schema[key]['max']}")

    print(f"\"{'Unknown' if 'title' not in book.keys() else book['title']}\" validation pass : {has_valid_schema}")
    return has_valid_schema