import crud
import os
import test_data
import unittest
import utils

class TestCrud(unittest.TestCase):

    def setUp(self):
        
        # test scenarios
        self.test_scenarios = ["valid_books", "invalid_books"]
        self.test_db_prefix = "books_test_db"

        # create test dbs
        for scenario in self.test_scenarios:
            db_name = f"{self.test_db_prefix}_{scenario}.json"
            utils.write_json(db_name, getattr(test_data, scenario))

        # corrupt json
        db_name = f"{self.test_db_prefix}_corrupt_json.json"
        with open(db_name,"w") as db:
            db.write(test_data.corrupt_json)
    
    def tearDown(self):
        for scenario in self.test_scenarios:
            db_name = f"{self.test_db_prefix}_{scenario}.json"
            if os.path.exists(db_name):
                os.remove(db_name)
        
        if os.path.exists(f"{self.test_db_prefix}_corrupt_json.json"):
            os.remove(f"{self.test_db_prefix}_corrupt_json.json")
    
    def test_load_books(self):
        
        # happy path
        scenario = self.test_scenarios[0]
        self.assertEqual(getattr(test_data, scenario), crud.load_books(f"{self.test_db_prefix}_{scenario}.json"))

        # load books fails if file doesn't exist
        self.assertEqual(False, crud.load_books("file_does_not_exist"))

        # check if load_books fails to read corrupt json
        self.assertEqual(False, crud.load_books(f"{self.test_db_prefix}_corrupt_json.json"))

if __name__ == "__main__":
    unittest.main()