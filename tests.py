import unittest
import os
from pprint_json import print_json

success_json = '''[
    {
        "root": {
            "child1": 1,
            "child2": 2,
            "child3": 3
        }
    }
]'''

test_file_success = 'success.json'
test_file_empty = 'empty.json'

class QuadraticEquationTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(test_file_success, 'w') as f:
            f.write('[{"root": {"child1":1, "child2":2, "child3": 3} }]')

        with open(test_file_empty, 'w') as f:
            f.write('')


    def test_print_json_not_found(self):
        self.assertEqual(print_json(''), 'File not found')


    def test_print_json_empty(self):
        self.assertEqual(print_json(test_file_empty), 'File is empty')


    def test_print_json_success(self):
        self.assertEqual(print_json(test_file_success), success_json)


    @classmethod
    def tearDownClass(cls):
        os.remove(test_file_success)
        os.remove(test_file_empty)

if __name__ == '__main__':
    unittest.main()

