# utility functions

import json

def read_json(fname):
    with open(fname, 'r') as file:
        books = json.load(file)
        return books
    

def write_json(fname, books):
    with open(fname, 'w') as file:
        json.dump(books, file, indent = 2)