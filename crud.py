import json
from validate import validate
from utils import read_json

BOOKS_FILE = "books.json"


def load_books():
    try:
        books = read_json(BOOKS_FILE)
        return books
    except FileNotFoundError:
        print(f"Failed to read db: '{BOOKS_FILE}'. file doesn't exist!")
        return False
    except json.decoder.JSONDecodeError:
        print(f"Failed to read db: '{BOOKS_FILE}'. json is corrupt!")
        return False
    except Exception as e:
        print(f"Failed to read db: '{BOOKS_FILE}'!")
        print(type(e), e)
        return False

def write_books():
    pass

def create(book):
    pass