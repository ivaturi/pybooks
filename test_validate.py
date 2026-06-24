import json
from validate import *
from test_data import valid_books, invalid_books

print("---- is_valid_book (valid books) ----")
for book in valid_books:
    is_valid_book(book)

print("---- is_valid_book (invalid books) ----")
for book in invalid_books:
    is_valid_book(book)

print("---- are_valid_books (valid books) ----")
validate(valid_books)