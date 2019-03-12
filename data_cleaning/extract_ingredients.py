import json

with open('no-dup-recipes.json') as f:
    recipes = json.load(f)

ingredients_sets = []
for recipe in recipes:
    ingredients = []
    for ingredient in recipe['ingredients']:
        ingredients.append(ingredient)
    ingredients_sets.append(ingredients)

with open('ingredients_sets.json', 'w') as data_file:
    json.dump(ingredients_sets, data_file)