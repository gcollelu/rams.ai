import json
import numpy as np
import scipy.stats as stats
import pylab as pl
import matplotlib.pyplot as plt
from collections import Counter

with open('final-recipes.json') as recipes_file:
    recipes = json.load(recipes_file)

print("We have ***" + str(len(recipes)) + "*** recipes")

# Counting duplicates
# dup_by_title = {}
# dup_count = 0
def count_unique_ingredients(recipes):
    unique_ingredients_count = 0
    unique_ingredients = set([])
    for i in range(len(recipes)):
        recipe = recipes[i]
        for ingredient in recipe['ingredients']:
            unique_ingredients.add(ingredient)
    return len(unique_ingredients)

print("****---- UNIQUE INGREDIENTS")
print(count_unique_ingredients(recipes))

ingredients_length = []
steps_length = []
for i in range(len(recipes)):
    ingredients_length.append(len(recipes[i]['ingredients']))
    steps_length.append(len(recipes[i]['steps']))
    # if recipes[i]['title'] in dup_by_title:
    #     dup_count += 1
    #     continue
ingredients_length = sorted(ingredients_length)
steps_length = sorted(steps_length)
ingr_counts = Counter(ingredients_length)
labels, values = zip(*ingr_counts.items())
# sort your values in descending order
indSort = np.argsort(values)[::-1]

# rearrange your data
labels = np.array(labels)[indSort]
values = np.array(values)[indSort]

indexes = np.arange(len(labels))

bar_width = 0.15

plt.bar(indexes, values)

plt.xlabel('Number of ingredients', fontsize=10)
plt.ylabel('Recipe count', fontsize=10)

# add labels
plt.xticks(indexes + bar_width, labels)
plt.show()

steps_counts = Counter(steps_length)
labels, values = zip(*steps_counts.items())
# sort your values in descending order
indSort = np.argsort(values)[::-1]

# rearrange your data
labels = np.array(labels)[indSort]
values = np.array(values)[indSort]

indexes = np.arange(len(labels))

bar_width = 0.15

plt.bar(indexes, values)

plt.xlabel('Number of steps', fontsize=10)
plt.ylabel('Recipe count', fontsize=10)

# add labels
plt.xticks(indexes + bar_width, labels)
plt.show()
# print(ingredients_length)
# print("With ***" + str(dup_count) + "*** duplicates")

print("Here is an example of what a recipe may look like")

print(json.dumps(recipes[55002], indent=2))

with open('ingredients_sets.json') as recipes_file:
    recipes = json.load(recipes_file)

print("We have ***" + str(len(recipes)) + "*** ingredients sets")


# print("Here is an example of what a recipe may look like")

# print(json.dumps(recipes[55002], indent=2))

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
