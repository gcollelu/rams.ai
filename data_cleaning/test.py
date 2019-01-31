import json

with open('recipes.json') as recipes_file:
    recipes = json.load(recipes_file)

print(json.dumps(recipes[127835], indent=2))

# def get_ingredients(recipe):
#     ingredients = []
#     for ingredient in recipe['ingredients']:
#         ingredients.append(ingredient['name'])
#     return ingredients

# def convert_to_classifier_format(recipe):
#     new_format_recipe = {'id': recipe['id'], 'ingredients': get_ingredients(recipe)}
#     return new_format_recipe

# abdos_recipes = []
# for recipe in recipes:
#     abdos_recipes.append(convert_to_classifier_format(recipe))

# with open('abdos_recipes.json', 'w') as abdos_recipes_file:
#     json.dump(abdos_recipes, abdos_recipes_file)
