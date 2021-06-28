import unittest
import sys
sys.path.append('../')
from utils.json_parser import *
from mock_data import *


class TestingJsonParser(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestingJsonParser, self).__init__(*args, **kwargs)

    def test_show_one_recipe_used_object_by_index(self):
        self.assertEqual(show_one_recipe_by_index(valid_json_response, 0)[0], function_response_index_0[0])

    def test_show_one_recipe_missed_object_by_index(self):
        self.assertEqual(show_one_recipe_by_index(valid_json_response, 0)[1], function_response_index_0[1])

    def test_show_one_recipe_title_by_index(self):
        self.assertEqual(show_one_recipe_by_index(valid_json_response, 0)[2], function_response_index_0[2])

    def test_show_one_recipe_used_object_by_index_1(self):
        self.assertEqual(show_one_recipe_by_index(valid_json_response, 1)[0], function_response_index_1[0])

    def test_show_one_recipe_missed_object_by_index_1(self):
        self.assertEqual(show_one_recipe_by_index(valid_json_response, 1)[1], function_response_index_1[1])

    def test_show_one_recipe_title_by_index_1(self):
        self.assertEqual(show_one_recipe_by_index(valid_json_response, 1)[2], function_response_index_1[2])

    def test_show_one_recipe_length_by_index(self):
        self.assertEqual(len(show_one_recipe_by_index(valid_json_response, 0)), len(function_response_index_0))

    def test_show_one_recipe_by_index_invalid_input_1(self):
        self.assertEqual(show_one_recipe_by_index(None, 0), (None, None, None))

    def test_show_one_recipe_by_index_invalid_index_1(self):
        self.assertEqual(show_one_recipe_by_index(valid_json_response, -1), (None, None, None))

    def test_show_one_recipe_by_index_invalid_index_2(self):
        self.assertEqual(show_one_recipe_by_index(valid_json_response, 101), (None, None, None))


if __name__ == '__main__':
    unittest.main()
