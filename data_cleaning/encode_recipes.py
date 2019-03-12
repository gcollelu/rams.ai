import json
import nltk
from tqdm import tqdm


'''
This script will encode our recipe dataset in the following way:

recipe: {
    'ingredients' : {
        ingredient_index : [[step_index1, step_position1], [step_index2, step_position2]]
    }
}

Where :
    ingredient_index : The index of the ingredient in the flat ingredients table
    step_index : The index of the step in the flat steps table
    step_position : The position in the order of steps in the recipe for the given step

- Each ingredient will have a set of steps that the ingredient is involved into
- Ingredients may have multiple steps
- Steps might use multiple ingredients

'''

with open('flat_steps.json') as flat_steps_file:
    flat_steps = json.load(flat_steps_file)

with open('flat_ingredients.json') as flat_ingredients_file:
    flat_ingredients = json.load(flat_ingredients_file)

with open('final-recipes.json') as recipes_file:
    recipes = json.load(recipes_file)

def steps_to_dict(flat_steps):
    print("steps_to_dict: START")
    steps = {}
    for i in tqdm(range(len(flat_steps))):
        steps[flat_steps[i]] = i
    
    return steps

def ingredients_to_dict(flat_ingredients):
    print("ingredients_to_dict: START")
    ingredients = {}
    for i in tqdm(range(len(flat_ingredients))):
        ingredients[flat_ingredients[i]] = {"i": i, "nouns": [word for (word, pos) in nltk.pos_tag(nltk.word_tokenize(flat_ingredients[i])) if (lambda pos: pos[:2] == 'NN')]}
    
    return ingredients

def generate_encoded_recipe(recipe, ingredients_dict, steps_dict):
    steps = recipe['steps']
    ingredients = recipe['ingredients']
    encoded_recipe = {}
    step_index = 1
    for step in steps:
        step_added = False
        step_nouns = [word for (word, pos) in nltk.pos_tag(nltk.word_tokenize(step)) if (lambda pos: pos[:2] == 'NN')]
        for step_noun in step_nouns:
            for ingredient in ingredients:
                if ingredients_dict[ingredient]["i"] not in encoded_recipe:
                    encoded_recipe[ingredients_dict[ingredient]["i"]] = []
                for ingredient_noun in ingredients_dict[ingredient]["nouns"]:
                    if step_noun == ingredient_noun:
                        encoded_recipe[ingredients_dict[ingredient]["i"]].append([steps_dict[step], step_index])
                        step_added = True
                        break
        if not step_added:
            for ingredient in ingredients:
                encoded_recipe[ingredients_dict[ingredient]["i"]].append([steps_dict[step], step_index])
        step_index += 1
        
    return encoded_recipe

def encode_recipes(recipes, ingredients_dict, steps_dict):
    encoded_recipes = []
    for recipe in tqdm(recipes):
        encoded_recipes.append(generate_encoded_recipe(recipe, ingredients_dict, steps_dict))
    return encoded_recipes

def decode_recipe(encoded_recipe, flat_ingredients, flat_steps):
    decoded_recipe = {}
    decoded_recipe["ingredients"] = set([])
    decoded_recipe["steps"] = set([])
    for ingredient_id in encoded_recipe:
        decoded_recipe["ingredients"].add(flat_ingredients[ingredient_id])
        for (step_id, position) in encoded_recipe[ingredient_id]:
            decoded_recipe["steps"].add((flat_steps[step_id], position))
    
    decoded_recipe["ingredients"] = list(decoded_recipe["ingredients"])
    decoded_recipe["steps"] = list(decoded_recipe["steps"])
    decoded_recipe['steps'] =  sorted(decoded_recipe['steps'], key=lambda tup: tup[1])
    decoded_recipe['steps'] = [ seq[0] for seq in decoded_recipe['steps'] ]

    return decoded_recipe

# print(json.dumps(recipes[55002], indent=2))
# encoded_recipe_test = generate_encoded_recipe(recipes[55002], ingredients_to_dict(flat_ingredients), steps_to_dict(flat_steps))
# print(encoded_recipe_test)
# decoded_recipe = decode_recipe(encoded_recipe_test, flat_ingredients, flat_steps)
# print(json.dumps(decoded_recipe, indent=2))
encoded_recipes = encode_recipes(recipes, ingredients_to_dict(flat_ingredients), steps_to_dict(flat_steps))

with open('encoded_recipes.json', 'w') as data_file:
    json.dump(encoded_recipes, data_file)
