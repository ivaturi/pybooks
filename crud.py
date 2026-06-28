import json
from utils import *
from validate import validate
from schema import SCHEMA as schema, VERSION


BOOKS_FILE = "books.json"


def load_books(books_db = BOOKS_FILE):
    try:
        books = read_json(books_db)
        return books
    except FileNotFoundError:
        print(f"Failed to read db: '{books_db}'. file doesn't exist!")
        return False
    except json.decoder.JSONDecodeError:
        print(f"Failed to read db: '{books_db}'. json is corrupt!")
        return False
    except Exception as e:
        print(f"Failed to read db: '{books_db}'!")
        print(type(e), e)
        return False

def write_books(books):
    try:
        write_json(BOOKS_FILE, books)
        print(f"Successfully wrote books to {BOOKS_FILE}")
        return True
    except Exception as e:
        print(f"Failed to write to db")
        print(type(e), e)
        return False

def create(newBook):

    # check if the book is valid
    if not validate([newBook]):
        print("Could not create book, because of validation errors")
        return False
   
    bookList = load_books()
    if bookList is False:
        print("Could not load books")
        return False

    # get required keys
    identity_keys = [key for key in schema.keys() if "identity" in schema[key] and schema[key]["identity"] == True]
    
    # check newBook against existing books for identity keys
    for book in bookList:
        match = True
        for key in identity_keys:
            match = match and newBook.get(key) == book.get(key)
        if match:
            print("Book with same title and author already exists")
            return False    
    
    # all tests pass. OK to add book
    bookList.append(newBook)
    return write_books(bookList)