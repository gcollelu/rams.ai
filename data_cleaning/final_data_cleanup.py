import json
import re

final = [] 

with open('no-dup-recipes.json') as recipes_file:
    recipes = json.load(recipes_file)

for i in range(len(recipes)):
    dirty_recipe = recipes[i]
    clean_recipe = {}
    clean_ingredients = []
    clean_recipe['id'] = dirty_recipe['id']
    clean_recipe['title'] = re.sub(r'[^a-zA-Z0-9]+', ' ', dirty_recipe['title'])
    for ingredient in dirty_recipe['ingredients']:
        if ingredient['name']:
            clean_ingredients.append(ingredient['name'])
    clean_recipe['ingredients'] = clean_ingredients
    clean_recipe['steps'] = dirty_recipe['steps']
    clean_recipe['rating'] = dirty_recipe['rating']
    final.append(clean_recipe)

with open('final-recipes.json', 'w') as recipes_file:
    json.dump(final, recipes_file)


