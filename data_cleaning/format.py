import json
import re


with open('data.json') as f:
    data = json.load(f)

# A function to print a dictionary object in an understandable way
def print_entry(idx):
   print(json.dumps(data[idx], indent=2))

# A helper function for debugging
def test_ingredients(idx):
   p = re.compile(r'^(?P<amount>(\d/\d)|(\d+(\s\d/\d)?))(\s(?P<unit>cup|teaspoon|tablespoon|pinch|pound|ounce)(s?))?(\s(\(.+\)))?(\s(?P<name>.+))?$', re.IGNORECASE)
   for ingredient in data[idx]['ingredients'] :
      print(re.match(p, ingredient).groupdict())

# Formats a single recipe into the wanted JSON format and returns the JSON as a dict
def format_recipe(idx):
   json_recipe = {}
   json_recipe['id'] = idx
   json_recipe['title'] = data[idx]['title']
   json_recipe['ingredients'] = []
   json_recipe['steps'] = []
   json_recipe['rating'] = data[idx]['rating_stars']
   # I made this RegEx
   # '^(?P<amount>(\d/\d)|(\d+(\s\d/\d)?))(\s(?P<unit>cup|teaspoon|tablespoon|pinch|pound)(s?))?(\s(?P<name>.+))?$'
   # It located amount, unit and name in an ingredient
   p = re.compile(r'^(?P<amount>(\d/\d)|(\d+(\s\d/\d)?))(\s(?P<unit>cup|teaspoon|tablespoon|pinch|pound|ounce)(s?))?(\s(\(.+\)))?(\s(?P<name>.+))?$', re.IGNORECASE)

   for ingredient in data[idx]['ingredients'] :
      ingredient_match = re.match(p, ingredient)
      if ingredient_match is not None:
         json_recipe['ingredients'].append(ingredient_match.groupdict())


   # Now I need to map each item in the list to a dictionary containing the 'idx' and 'content'
   for i in range(len(data[idx]['instructions'])):
      json_recipe['steps'].append({'idx': i+1, 'content': data[idx]['instructions'][i]})
   return json_recipe


def format_recipes():
   json_recipes = []
   for i in range(len(data)):
      json_recipes.append(format_recipe(i))
   return json_recipes


formatted_recipes = format_recipes()
with open('recipes.json', 'w') as recipes_file:
    json.dump(formatted_recipes, recipes_file)