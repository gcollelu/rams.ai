import json
import re

raw_data = []
dup_by_title = {}
no_dup_recipes = []
with open('final-recipes-lots-of-steps.json') as f:
    data = json.load(f)


# Counting duplicates
dup_count = 0
for i in range(len(data)):
    if data[i]['title'] in dup_by_title:
        dup_count += 1
        dup_by_title[data[i]['title']] += 1
        continue
    #delete recipes with extra ingredients
    if len(data[i]['ingredients']) > 15 or len(data[i]['ingredients']) <= 1:
        continue
    # deleting recipes with  extra steps
    if len(data[i]['steps']) > 20 or len(data[i]['steps']) <= 1:
        continue
    dup_by_title[data[i]['title']] = 0
    steps = data[i]['steps']
    # Split steps into sentences
    # new_steps = []
    # for step in steps:
    #     content = step['content']
    #     for sentence in re.split(r"\.|\?|\!",content):
    #         sentence = sentence.strip()
    #         new_steps.append(sentence)
    # data[i]['steps'] = new_steps
    # only append if there are no dups
    # Don't use empty steps
    new_steps = []
    for step in steps:
        if step :
            new_steps.append(step)
    data[i]['steps'] = new_steps

    no_dup_recipes.append(data[i])

# Duplicates: 137872
print("Duplicates: " + str(dup_count))


# for element in raw_data:
    
    
with open('no-dup-recipes.json', 'w') as data_file:
    json.dump(no_dup_recipes, data_file)