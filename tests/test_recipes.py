import unittest
import sys
sys.path.append('../')
from controller.recipes import *
from mock_data import *


class TestingRecipesAppFunctionality(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestingRecipesAppFunctionality, self).__init__(*args, **kwargs)
        self.recipes=Recipes()

    def test_parse_shopping_list_function_empty_list(self):
        self.assertEqual(parse_shopping_list([]), empty_shopping_list_response)

    def test_parse_single_shopping_list_function(self):
        self.assertEqual(parse_shopping_list(shopping_list_1), parse_shopping_list_1_response)

    def test_parse_multi_shopping_list_function(self):
        self.assertEqual(parse_shopping_list(shopping_list_2), parse_shopping_list_2_response)

    def test_check_total_data_response_none(self):
        self.assertEqual(self.recipes.check_total_data_response(None), None)

    def test_check_and_assign_ingredient_number_1(self):
        self.assertEqual(check_and_assign_ingredient_number(ingredient_number=10), 10)

    def test_check_and_assign_ingredient_number_2(self):
        self.assertEqual(check_and_assign_ingredient_number(ingredient_number=100), 100)

    def test_check_and_assign_ingredient_number_invalid_1(self):
        self.assertEqual(check_and_assign_ingredient_number(ingredient_number=0), 1)

    def test_check_and_assign_ingredient_number_invalid_2(self):
        self.assertEqual(check_and_assign_ingredient_number(ingredient_number=-10), 1)

    def test_check_and_assign_ingredient_number_invalid_3(self):
        self.assertEqual(check_and_assign_ingredient_number(ingredient_number=101), 100)


if __name__ == '__main__':
    unittest.main()
