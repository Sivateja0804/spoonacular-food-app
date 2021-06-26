from app.recipes import Recipes

if __name__=="__main__":
    print("Welcome to Spoonacular Food App")
    recipe_object=Recipes()
    recipe_object.get_receipes()
