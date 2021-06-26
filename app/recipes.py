from app.restAPI import Requests
from app.parseJson import JsonParser


class Recipes:
    def __init__(self):
        self.json=JsonParser()
        self.req = Requests()

    def get_ingredients(self):
        # todo handle exceptions properly
        # todo clean the input data
        try:
            print("Please type the ingredients with comma separated (ex: apple, banana, Mango) to search for recipes")
            ingredients = input("Enter here: ")
            ingredients = ingredients.split(",")
            for i in range(len(ingredients)):
                ingredients[i] = ingredients[i].strip()
        except:
            print("Please type in the correct format")
            ingredients = self.get_ingredients()
        return ingredients

    def search_new_recipe(self, title, exclude_cuisine, req):
        exclude_cuisine.append(title)
        ingredients = self.get_ingredients()
        used_object, missed_object, unused_object, title, = req.get_and_show_one_recipe_complexsearch(ingredients,
                                                                                                      number=1)
        return used_object, missed_object, unused_object, title, exclude_cuisine

    def parse_shopping_list(self, shopping_list):
        shopping_items = []
        aisle = []
        amount = 0.0
        for missed_object in shopping_list:
            for missingItem in missed_object:
                shopping_items.append(missingItem["name"])
                aisle.append(missingItem["aisle"])
                amount += missingItem["amount"]
        return shopping_items, aisle, amount

    def show_shopping_list(self, shopping_list):
        shopping_items, aisle, amount = self.parse_shopping_list(shopping_list)
        shopping_items = set(shopping_items)
        shopping_items_string = ",".join(shopping_items)
        print("Shopping Items List: ")
        print(shopping_items_string)
        aisle = set(aisle)
        aisle_string = ",".join(aisle)
        print("Visit below Aisles: ")
        print(aisle_string)
        print("Total Amount: " + str(amount))

    def get_input_yes_no(self):
        try:
            response = input("Enter 1 for Yes and 2 for No:")
            if response not in ["1", "2"]:
                print("Please type the input in correct format ex: 1 or 2")
                response = self.get_input_yes_no()
        except:
            print("Please type the input in correct format ex: 1 or 2")
            response = self.get_input_yes_no()
        return response

    def get_receipes(self):
        ingredients = self.get_ingredients()
        total_data = self.req.get_requests(ingredients, number=100)
        if not total_data:
            print("There are no recipe with this ingredient. Please use proper ingredients: ex: apple, banana, etc")
            return self.get_receipes()
        shopping_list = []
        index = 0
        n = len(total_data)
        while index < n:
            print("-------------------------------------------------------------------------")
            used_object, missed_object, title = self.json.show_one_recipe_by_index(total_data, index)
            index += 1
            print("Do you like the recipe?")
            response = self.get_input_yes_no()
            if response == "1":
                print(
                    "\nIt's great that you liked the recipe! The missing items have been added to your shopping list\n")
                print("Do you want to search for more recipes?")
                shopping_list.append(missed_object)
                more_recipes = self.get_input_yes_no()
                if more_recipes == "2":
                    break
                elif more_recipes == "1":
                    continue
            elif response == "2":
                print("We are sorry that you didn't like our recipe. We are showing you a new recipe")
                continue
        if shopping_list:
            self.show_shopping_list(shopping_list)
        else:
            print("There are no Items to Shop")
