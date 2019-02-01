import json
import csv

input_file=open('recipes.json', 'r')
raw_data=json.load(input_file)
csvFile="submission.csv"

result = []
for item in raw_data:
    ingredients = []
    my_dict={}
    my_dict['id']=item['id']
    my_dict['title']=item['title']
    my_dict['ingredients'] = item['ingredients']
    my_dict['steps']=item['steps']
    my_dict['rating']=item['rating']

    reader = csv.reader(open(csvFile, 'r'))
    for data in reader:
        if data[0] == my_dict['id']:
            my_dict['cuisine'] = data[1]
            break

    if 'cuisine' in my_dict:
        result.append(my_dict)
    #else:
        #print ("ID: " + str(item['id']))
    
with open('final_recipes.json', 'w') as data_file:
    json.dump(result, data_file)