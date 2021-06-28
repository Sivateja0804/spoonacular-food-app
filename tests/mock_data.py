valid_json_response = [{"id": 665469, "title": "Xocai Healthy Chocolate Peanut Butter Bannana Dip",
                        "image": "https://spoonacular.com/recipeImages/665469-312x231.jpg",
                        "imageType": "jpg", "usedIngredientCount": 1, "missedIngredientCount": 2,
                        "missedIngredients": [
                            {"id": 19081, "amount": 1.0, "unit": "", "unitLong": "", "unitShort": "",
                             "aisle": "Sweet Snacks", "name": "chocolate",
                             "original": "1 chunk Chocolate (Xocai Nugget)",
                             "originalString": "1 chunk Chocolate (Xocai Nugget)",
                             "originalName": "Chocolate (Xocai Nugget)",
                             "metaInformation": ["chunk", "(Xocai Nugget)"],
                             "meta": ["chunk", "(Xocai Nugget)"],
                             "image": "https://spoonacular.com/cdn/ingredients_100x100/milk-chocolate.jpg"},
                            {"id": 16098, "amount": 1.0, "unit": "tbsp", "unitLong": "tablespoon",
                             "unitShort": "Tbsp", "aisle": "Nut butters, Jams, and Honey",
                             "name": "peanut butter",
                             "original": "1 tbsp Peanut Butter (Natural Peanut Butter)",
                             "originalString": "1 tbsp Peanut Butter (Natural Peanut Butter)",
                             "originalName": "Peanut Butter (Natural Peanut Butter)",
                             "metaInformation": ["(Natural Peanut Butter)"],
                             "meta": ["(Natural Peanut Butter)"],
                             "image": "https://spoonacular.com/cdn/ingredients_100x100/peanut-butter.png"}],
                        "usedIngredients": [
                            {"id": 9040, "amount": 1.0, "unit": "", "unitLong": "", "unitShort": "",
                             "aisle": "Produce", "name": "bananas",
                             "original": "1 stem Bananas (Banana, peeled)",
                             "originalString": "1 stem Bananas (Banana, peeled)",
                             "originalName": "stem Bananas (Banana, peeled)",
                             "metaInformation": ["peeled", "(Banana, )"], "meta": ["peeled", "(Banana, )"],
                             "image": "https://spoonacular.com/cdn/ingredients_100x100/bananas.jpg"}],
                        "unusedIngredients": [], "likes": 1},
                       {"id": 650485, "title": "Luscious Orange Cardamom Smoothie",
                        "image": "https://spoonacular.com/recipeImages/650485-312x231.jpg",
                        "imageType": "jpg", "usedIngredientCount": 1, "missedIngredientCount": 2,
                        "missedIngredients": [
                            {"id": 9206, "amount": 0.5, "unit": "cup", "unitLong": "cups",
                             "unitShort": "cup", "aisle": "Beverages", "name": "orange juice",
                             "original": "1/2 cup orange juice, fresh preferred but bottled will work too. (I suggest starting with 1/4 cup orange juice and adding the rest slowly according to preference )",
                             "originalString": "1/2 cup orange juice, fresh preferred but bottled will work too. (I suggest starting with 1/4 cup orange juice and adding the rest slowly according to preference )",
                             "originalName": "orange juice, fresh preferred but bottled will work too. (I suggest starting with 1/4 cup orange juice and adding the rest slowly according to preference )",
                             "metaInformation": ["fresh",
                                                 "with 1/4 cup orange juice and adding the rest slowly according to preference )"],
                             "meta": ["fresh",
                                      "with 1/4 cup orange juice and adding the rest slowly according to preference )"],
                             "extendedName": "fresh orange juice",
                             "image": "https://spoonacular.com/cdn/ingredients_100x100/orange-juice.jpg"},
                            {"id": 2006, "amount": 1.0, "unit": "pinch", "unitLong": "pinch",
                             "unitShort": "pinch", "aisle": "Spices and Seasonings",
                             "name": "cardamom powder",
                             "original": "Pinch of cardamom powder (Cardamom powder is very strong so add only a pinch)",
                             "originalString": "Pinch of cardamom powder (Cardamom powder is very strong so add only a pinch)",
                             "originalName": "Pinch of cardamom powder (Cardamom powder is very strong so add only a pinch)",
                             "metaInformation": ["(Cardamom powder is very strong so add only a pinch)"],
                             "meta": ["(Cardamom powder is very strong so add only a pinch)"],
                             "image": "https://spoonacular.com/cdn/ingredients_100x100/cardamom.jpg"}],
                        "usedIngredients": [
                            {"id": 9040, "amount": 2.0, "unit": "", "unitLong": "", "unitShort": "",
                             "aisle": "Produce", "name": "bananas",
                             "original": "2 bananas, frozen, cut in chunks",
                             "originalString": "2 bananas, frozen, cut in chunks",
                             "originalName": "bananas, frozen, cut in chunks",
                             "metaInformation": ["frozen", "cut in chunks"],
                             "meta": ["frozen", "cut in chunks"], "extendedName": "frozen bananas",
                             "image": "https://spoonacular.com/cdn/ingredients_100x100/bananas.jpg"}],
                        "unusedIngredients": [], "likes": 1}]

function_response_index_0 = [[{'aisle': 'Produce', 'amount': 1.0, 'name': 'bananas'}],
                             [{'aisle': 'Sweet Snacks', 'amount': 1.0, 'name': 'chocolate'},
                              {'aisle': 'Nut butters, Jams, and Honey',
                               'amount': 1.0,
                               'name': 'peanut butter'}],
                             'Xocai Healthy Chocolate Peanut Butter Bannana Dip']

function_response_index_1 = [[{'aisle': 'Produce', 'amount': 2.0, 'name': 'bananas'}],
                             [{'aisle': 'Beverages', 'amount': 0.5, 'name': 'orange juice'},
                              {'aisle': 'Spices and Seasonings', 'amount': 1.0, 'name': 'cardamom powder'}],
                             'Luscious Orange Cardamom Smoothie']

missed_object_0 = function_response_index_0[1]
missed_object_1 = function_response_index_1[1]

empty_shopping_list_response = ([], [], 0.0)

shopping_list_1 = [missed_object_0]
parse_shopping_list_1_response = (['chocolate', 'peanut butter'],
                                  ['Sweet Snacks', 'Nut butters, Jams, and Honey'],
                                  2.0)

shopping_list_2 = [missed_object_0, missed_object_1]
parse_shopping_list_2_response = (['chocolate', 'peanut butter', 'orange juice', 'cardamom powder'],
                                  ['Sweet Snacks',
                                   'Nut butters, Jams, and Honey',
                                   'Beverages',
                                   'Spices and Seasonings'],
                                  3.5)
