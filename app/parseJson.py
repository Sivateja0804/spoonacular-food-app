class JsonParser:
    def show_one_recipe_by_index(self, total_data, i):
        data = total_data[i]
        title = data["title"]
        print("Recipe: " + title)
        used_ingredients = data["usedIngredients"]
        missed_ingredients = data["missedIngredients"]
        used_object = self.show_receipes(used_ingredients, "used", [], "Used Ingredients: ")
        missed_object = self.show_receipes(missed_ingredients, "missed", [], "Missing Ingredients you need to shop: ")
        return used_object, missed_object, title

    def show_receipes(self, ingredients, action, ingredient_object, print_message):
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
