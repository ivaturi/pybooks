# utility functions

import json

def read_json(fname):
    with open(fname, 'r') as file:
        books = json.load(file)
        return books
    