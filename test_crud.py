from test_data import valid_books
from crud import load_books, write_books, create
from validate import *

# test load_books by validating
books = load_books()
validate(books)

# test that the list of valid books can be written
write_books(valid_books)

# test that a book caa be created and added to the db
book = valid_books[0]
print(create(book))