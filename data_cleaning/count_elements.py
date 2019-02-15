import json

input_file=open('final_recipes_classified.json', 'r')
raw_data=json.load(input_file)

result = 0
for item in raw_data:
    if (item['id'] == 155324):
        json.dumps(item['id'], indent=2)
    result+=1

print(result)