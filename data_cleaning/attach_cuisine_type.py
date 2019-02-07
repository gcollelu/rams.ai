import json
import csv

input_file=open('recipes.json', 'r')
raw_data=json.load(input_file)
csvFile="submission.csv"

reader = csv.reader(open(csvFile, 'r'))
cuisines={}
for data in reader:
    dataid = data[0]
    cuisines[dataid]= data[1]

#print(cuisines['220028'])
result = []
for item in raw_data:
    ingredients = []
    my_dict={}
    my_dict['id']=item['id']
    my_dict['title']=item['title']
    my_dict['ingredients'] = item['ingredients']
    my_dict['steps']=item['steps']
    my_dict['rating']=item['rating']

    itemid = str(my_dict['id'])
    if itemid in cuisines:
        #print("ha")
        my_dict['cuisine'] = cuisines[itemid]
        result.append(my_dict)
    #else:
        #print ("ID: " + str(item['id']))
    
with open('final_recipes.json', 'w') as data_file:
    json.dump(result, data_file)