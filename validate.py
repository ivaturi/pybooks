import json
from schema import SCHEMA as schema, VERSION

def validate(book):
    
    # get all schema keys
    schema_keys = schema.keys()

    # get required keys
    required_keys = []
    for key in schema_keys:
        if schema[key]["required"] == True:
            required_keys.append(key)

    print(">  Validating..........", end="")
    # check book keys
    r_keys = 0
    for key in list(book):
        if key not in schema_keys:
            print(f"NOK: invalid key found: {key}")
            return False

    # check required keys
    for key in required_keys:    
        if key not in book:
            print(f"NOK: required key [{key}] not found!")
            return False

    
    print("OK")
    return True


book = {
    "title": "The Name of the Rose",
    "author": "Umberto Eco",
    "last_read": "2023-11",
    "format": "physical",
    "genres": ["historical fiction", "mystery"],
    "rating": 5,
    "takeaway": "Semiotics is everywhere once you start looking."
}


validate(book)