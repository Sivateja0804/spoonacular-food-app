import requests


class Requests:
    def __init__(self):
        self.findByIngredientsURl = "https://api.spoonacular.com/recipes/findByIngredients"
        self.apiKey = "306223d5987944d18b62f529be3a363d"

    # get requests by ingredients input=ingredients,number output=Json data with recipes
    def get_requests(self, ingredients, number=10):
        PARAMS = {'ingredients': ingredients,
                  'number': number,
                  'apiKey': self.apiKey}
        respone = requests.get(url=self.findByIngredientsURl, params=PARAMS)
        if respone.status_code != 200:
            return "Invalid error exception"
        data = respone.json()
        return data


