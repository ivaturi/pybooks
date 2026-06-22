from test_data import valid_books
from crud import load_books, write_books

books = load_books()
print(books)

write_books(valid_books)