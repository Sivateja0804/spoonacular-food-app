import requests
import os
from dotenv import load_dotenv
from utils.app_constants import *


class Requests:
    def __init__(self):
        load_dotenv()
        self.findByIngredientsURl = FIND_BY_INGREDIENTS_URL
        self.apiKey = os.getenv('API_KEY')

    # get requests by ingredients input=ingredients,number output=Json data with recipes
    def get_requests(self, ingredients, number=10):
        try:
            params = {'ingredients': ingredients,
                      'number': number,
                      'apiKey': self.apiKey}
            response = requests.get(url=self.findByIngredientsURl, params=params)
            if response.status_code != 200:
                response.raise_for_status()
            data = response.json()
            return data
        except Exception as e:
            print(e)
            return None
