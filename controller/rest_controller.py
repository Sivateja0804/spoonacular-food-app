import requests
import os
from dotenv import load_dotenv
from utils.app_constants import *


class Requests:
    def __init__(self):
        load_dotenv()
        self.findByIngredientsURl = FIND_BY_INGREDIENTS_URL
        self.apiKey = os.getenv('API_KEY')

    '''
    Use some of the supplied ingredients and requests the url to get the Recipe response
    @param ingredients {Object} - Object with all the user entered ingredients 
    @param number {Integer} - The maximum number of recipes to return
    
    @param data {Object} - Json response which contains recipe data
    '''
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
