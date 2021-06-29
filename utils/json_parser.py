"""
take ingredients and shows used ingredients if the action is used
take ingredients and show missed ingredients, aisle, amount if the action is missed
@param ingredients {Object} - Object with either used or missed ingredient details
@param action {String} - used or missed
@param ingredient_object {Object} - empty list to store the ingredient details
@param print_message {String} - Message to show what action that is currently being performed
"""
def show_recipes(ingredients, action, ingredient_object, print_message):
    print_statement = []
    for i, ingredient in enumerate(ingredients):
        amount = ingredient["amount"]
        aisle = ingredient["aisle"]
        name = ingredient["name"]
        if action == "used":
            print_statement.append(name)
        elif action == "missed":
            print_statement.append(
                "Item" + str(i + 1) + ": " + name + ", Amount: " + str(amount) + ", Aisle: " + aisle)
        ingredient_object.append({"amount": amount, "aisle": aisle, "name": name})
    print(print_message)
    if action == "missed":
        for statement in print_statement:
            print(statement)
    elif action == "used":
        if print_statement:
            print_statement = ",".join(print_statement)
            print(print_statement)
        else:
            print("No " + action + " ingredients")
    print()
    return ingredient_object


"""
find recipe object by index, parse it and return the used, missed and title 
@param total_data {Object} - complete Json response object with all the recipes details
@param i {Integer} - index to get the recipe

@param used_object {Object} - Used ingredient details
@param missed_object {Object} - Missing ingredient item details
@param title {String} - Name of the recipe
"""
def show_one_recipe_by_index(total_data, i):
    used_object, missed_object, title = None, None, None
    if total_data and 0 <= i < len(total_data):
        try:
            data = total_data[i]
            title = data["title"]
            print("Recipe: " + title)
            used_ingredients = data["usedIngredients"]
            missed_ingredients = data["missedIngredients"]
            used_object = show_recipes(used_ingredients, "used", [], "Used Ingredients: ")
            missed_object = show_recipes(missed_ingredients, "missed", [], "Missing Ingredients you need to shop: ")
        except Exception:
            pass
    return used_object, missed_object, title
