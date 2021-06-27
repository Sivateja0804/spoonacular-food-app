import requests


class Requests:
    def __init__(self):
        self.findByIngredientsURl = "https://api.spoonacular.com/recipes/findByIngredients"
        self.apiKey = "306223d5987944d18b62f529be3a363d"

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