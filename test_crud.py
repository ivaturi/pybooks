from test_data import valid_books
from crud import load_books, write_books
from validate import validate

validate(load_books())
write_books(valid_books)