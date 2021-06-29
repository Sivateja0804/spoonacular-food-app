from controller.rest_controller import Requests
from utils.json_parser import *
from utils.app_constants import *

'''
Parse the shopping list object which has all the missing ingredients and returns the shopping,
aisle lists and  the total amount.
@param shopping_list {Object} - Object with all the missing ingredients objects

@return shopping_items {Object} - list that stores all the missing ingredients names
@return aisle {Object} - list that stores all the missing ingredients aisles
@return amount {float} - total expected amount required to shop the missing ingredients
'''
def parse_shopping_list(shopping_list):
    shopping_items = []
    aisle = []
    amount = 0.0
    for missed_object in shopping_list:
        for missingItem in missed_object:
            shopping_items.append(missingItem["name"])
            aisle.append(missingItem["aisle"])
            amount += missingItem["amount"]
    return shopping_items, aisle, amount


'''
Parse shopping list and show the shopping items, aisles and total amount to user
@param shopping_list {Object} - Object with all the missing ingredients objects
'''
def show_shopping_list(shopping_list):
    try:
        shopping_items, aisle, amount = parse_shopping_list(shopping_list)
        shopping_items_dict = {}
        for item in shopping_items:
            shopping_items_dict[item] = shopping_items_dict.get(item, 0) + 1
        shopping_items_string = ""
        for item,count in shopping_items_dict.items():
            shopping_items_string+=item+" :"+str(count)+", "
        if shopping_items_string:
            shopping_items_string=shopping_items_string[:-2]
        print("Shopping Items List with quantity: ")
        print(shopping_items_string)
        aisle = set(aisle)
        aisle_string = ",".join(aisle)
        print("Visit below Aisles: ")
        print(aisle_string)
        print("Total Amount: " + str(amount))
    except Exception:
        print("Sorry, Unable to show shopping list.")


'''
This function makes sures the ingredient number lies between 1-100
@param RECIPES_NUMBER {Integer} - Its value is in app_constant.py file. The maximum number of recipes to return
@return {Integer}- ranges from 1-100 inclusive
'''
def restrict_recipe_number(recipe_number=RECIPES_NUMBER):
    return min(max(1, recipe_number), 100)


class Recipes:
    def __init__(self):
        self.req = Requests()

    '''
    This function return ingredients list that were entered in the command line.
    @return ingredients {Object} - List of ingredient names
    '''
    def get_ingredients(self):
        try:
            print("Please type the ingredients with comma separated (ex: apple, banana, Mango) to search for recipes")
            ingredients = input("Enter here: ")
            ingredients = ingredients.split(",")
            for i in range(len(ingredients)):
                ingredients[i] = ingredients[i].strip()
        except ValueError:
            print("Please type in the correct format")
            ingredients = self.get_ingredients()
        return ingredients

    '''
        This function takes input 1 or 2 from terminal and return same response
        @return response {String} - 1 for Yes and 2 for No
    '''
    def get_input_yes_no(self):
        try:
            response = input("Enter 1 for Yes and 2 for No:")
            if response not in ["1", "2"]:
                print("Please type the input in correct format ex: 1 or 2")
                response = self.get_input_yes_no()
        except ValueError:
            print("Please type the input in correct format ex: 1 or 2")
            response = self.get_input_yes_no()
        return response

    '''
        This function validates total_data. if it is None, There will be issue with the applicationto access url
        if total_data is empty_list then user entered incorrect ingredients so we till him to enter properly again
        @param total_data {Object} - complete Json response object with all the recipes details
    '''
    def check_total_data_response(self, total_data):
        if total_data is None:
            print("We're so sorry, something went wrong. Please check later.")
            return total_data
        if not total_data:
            print("There are no recipe with this ingredient. Please use proper ingredients: ex: apple, banana, etc")
            return self.get_recipes()

    '''This function show the user a recipe that contains some of the supplied ingredients. If the user likes the 
    recipe, it add the missing ingredients to a shopping list If the user does not like the recipe, it give the user a new 
    recipe. It Repeat the process of showing new recipes to the user and adding the missing ingredients of “liked” 
    recipes until the user is satisfied with their shopping list and shows the shopping list at the end.
    @param total_data {Object} - complete Json response object with all the recipes details. '''
    def validate_data_and_add_items_to_shopping_cart(self, total_data):
        if total_data:
            shopping_list = []
            index = 0
            n = len(total_data)
            while index < n:
                print("-------------------------------------------------------------------------")
                used_object, missed_object, title = show_one_recipe_by_index(total_data, index)
                index += 1
                if used_object is None or title is None or missed_object is None:
                    continue
                print("Do you like the recipe?\n")
                response = self.get_input_yes_no()
                if response == "1":
                    if missed_object:
                        print(
                            "It's great that you liked the recipe! The missing items have been added to your shopping "
                            "list.\nDo you want to search for more recipes?\n")
                        shopping_list.append(missed_object)
                    else:
                        print("There are no items to add to shopping cart. Do you want to search for more recipes?\n")

                    more_recipes = self.get_input_yes_no()
                    if more_recipes == "2":
                        break
                    elif more_recipes == "1":
                        continue
                elif response == "2":
                    print("We are sorry that you didn't like our recipe. We are showing you a new recipe")
                    continue
            if index >= n:
                print("Sorry there are no more recipes to show")
            if shopping_list:
                show_shopping_list(shopping_list)
            else:
                print("Shopping list is empty")
        else:
            self.check_total_data_response(total_data)

    '''This function first let user type the ingredients and then use this data to get the recipe details and perform 
    all the main app logic and show the shopping list details to the user '''
    def get_recipes(self):
        ingredients = self.get_ingredients()
        total_data = self.req.get_requests(ingredients, number=restrict_recipe_number())
        self.validate_data_and_add_items_to_shopping_cart(total_data)
