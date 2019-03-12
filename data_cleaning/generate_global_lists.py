import json

with open('final-recipes.json') as recipes_file:
    recipes = json.load(recipes_file)


def generate_global_ingredients(recipes):
    unique_ingredients = set([])
    for i in range(len(recipes)):
        recipe = recipes[i]
        for ingredient in recipe['ingredients']:
            unique_ingredients.add(ingredient)
    return list(unique_ingredients)


def generate_global_steps(recipes):
    unique_steps = set([])
    for i in range(len(recipes)):
        recipe = recipes[i]
        for ingredient in recipe['steps']:
            unique_steps.add(ingredient)
    return list(unique_steps)

with open('flat_ingredients.json', 'w') as data_file:
    json.dump(generate_global_ingredients(recipes), data_file)

with open('flat_steps.json', 'w') as data_file:
    json.dump(generate_global_steps(recipes), data_file)

