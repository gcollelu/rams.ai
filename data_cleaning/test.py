import json

with open('recipes.json') as recipes_file:
    recipes = json.load(recipes_file)

print(json.dumps(recipes[4], indent=2))