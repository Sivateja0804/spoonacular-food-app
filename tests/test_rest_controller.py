import unittest
from controller.rest_controller import Requests


class TestingAPIResponse(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestingAPIResponse, self).__init__(*args, **kwargs)
        self.req = Requests()

    def test_json_response_length_100(self):
        ingredients = ["apple", "banana", "mango"]
        self.assertEqual(len(self.req.get_requests(ingredients, number=100)), 100)

    def test_json_response_length_50(self):
        ingredients = ["apple", "banana", "mango"]
        self.assertEqual(len(self.req.get_requests(ingredients, number=50)), 50)

    def test_json_response_length_10(self):
        ingredients = ["apple", "banana", "mango"]
        self.assertEqual(len(self.req.get_requests(ingredients, number=10)), 10)

    def test_json_response_length_1(self):
        ingredients = ["apple", "banana", "mango"]
        self.assertEqual(len(self.req.get_requests(ingredients, number=1)), 1)

    def test_invalid_ingredients_input(self):
        ingredients = ["xcvbn", "@#$%^&", "!!!!!!!!"]
        self.assertEqual(len(self.req.get_requests(ingredients, number=10)), 0)

    def test_invalid_ingredients_input_with_empty_spaces(self):
        ingredients = ["      ", "       ", "        "]
        self.assertEqual(len(self.req.get_requests(ingredients, number=10)), 0)

    def test_invalid_ingredients_input_empty_string(self):
        ingredients = [""]
        self.assertEqual(self.req.get_requests(ingredients, number=10), [])

    def test_json_response_invalid_number_less_than_zero(self):
        ingredients = ["banana","apple"]
        self.assertEqual(len(self.req.get_requests(ingredients, number=-1)), 1)

    def test_json_response_invalid_number_greater_than_zero(self):
        ingredients = ["banana","apple"]
        self.assertEqual(len(self.req.get_requests(ingredients, number=1000)), 100)

    def test_json_response_single_ingredient(self):
        ingredients = ["banana"]
        self.assertEqual(len(self.req.get_requests(ingredients, number=10)), 10)

    def test_json_response_invalid_url(self):
        request = Requests()
        request.findByIngredientsURl += "345;"
        ingredients = ["banana", "apple"]
        self.assertEqual(request.get_requests(ingredients, number=10), None)

    def test_json_response_invalid_apikey(self):
        request = Requests()
        request.apiKey = "cxzvbnm"
        ingredients = ["banana", "apple"]
        self.assertEqual(request.get_requests(ingredients, number=10), None)


if __name__ == '__main__':
    unittest.main()
