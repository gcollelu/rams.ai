import json

input_file=open('final_recipes.json', 'r')
raw_data=json.load(input_file)

result = 0
for item in raw_data:
    result+=1

print(result)