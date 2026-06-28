import crud
import os
import test_data
import unittest
import utils
from unittest.mock import patch


class TestCrud(unittest.TestCase):

    def setUp(self):
        
        self.test_db = "books_test_db.json"
        utils.write_json(self.test_db, test_data.valid_books)    
        self.print_patch = patch("builtins.print")
        self.print_patch.start()

    def tearDown(self):
        if os.path.exists(self.test_db):
            os.remove(self.test_db)
        self.print_patch.stop()

    
    def test_load_valid_books(self):
        # happy path
        utils.write_json(self.test_db, test_data.valid_books)
        self.assertEqual(test_data.valid_books, crud.load_books(self.test_db))
   
    def test_load_from_nonexistent_file(self):
        # load books fails if file doesn't exist
        self.assertEqual(False, crud.load_books("file_does_not_exist"))

    def test_load_corrupt_json(self):
        # corrupt json
        with open(self.test_db,"w") as db:
            db.write(test_data.corrupt_json)
        
        self.assertEqual(False, crud.load_books(self.test_db))


    def test_create_valid_book(self):
        # clean slate
        utils.write_json(self.test_db, [])
        # grab a valid book entry
        book = test_data.valid_books[0]
        self.assertEqual(True, crud.create(book, self.test_db))
        books = crud.load_books(self.test_db)
        self.assertIn(book, books)
        

    def test_create_invalid_book(self):
        utils.write_json(self.test_db, [])
        invalid_book = {"title" : "Invalid book", "status": "invalid status"}
        self.assertEqual(False, crud.create(invalid_book, self.test_db))
        books = crud.load_books(self.test_db)
        self.assertNotIn(invalid_book, books)

    def test_create_existing_book(self):
        utils.write_json(self.test_db, test_data.valid_books)
        existing_book = test_data.valid_books[2]
        self.assertEqual(False, crud.create(existing_book, self.test_db))
        books = crud.load_books(self.test_db)
        self.assertIn(existing_book, books)

    

if __name__ == "__main__":
    unittest.main()