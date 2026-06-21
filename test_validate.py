import json
from validate import validate
from test_data import valid_books, invalid_books

for book in valid_books:
    validate(book)

for book in invalid_books:
    validate(book)