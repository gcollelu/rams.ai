import json

input_file=open('recipes.json', 'r')
raw_data=json.load(input_file)
output_file_name = "cleaned_recipes1.json"

result = []
for item in raw_data:
    ingredients = []
    my_dict={}
    my_dict['id']=item['id']
    my_dict['ingredients'] = []
    for ingredient in item['ingredients']:
        if (ingredient is not None):
            my_dict['ingredients'].append(ingredient)
        #else:
        #    print ("null ingredient ID: " + str(item['id']))
    #print(my_dict)
    if (len(my_dict['ingredients']) == 0):
        print ("ID: " + str(item['id']))
    else:
        result.append(my_dict)
        #if (len(result) == 10000):
        #    with open(output_file_name, 'w') as data_file:
        #        json.dump(result, data_file)
        #    output_file_name += "1"
        #    result = []

    
with open('cleaned_recipes.json', 'w') as data_file:
    json.dump(result, data_file)