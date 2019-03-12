import json

raw_data = []
data_by_title = {}
result = []
with open('data.json') as f:
    for line in f:
        raw_data.append(json.loads(line))


# Counting duplicates
dup_count = 0
for i in range(len(raw_data[0])):
    if raw_data[0][i]['title'] in data_by_title:
        dup_count += 1
        data_by_title[raw_data[0][i]['title']] += 1
        continue
    data_by_title[raw_data[0][i]['title']] = 0

# Duplicates: 137872
for title in data_by_title:
    if data_by_title[title] > 1 :
        print(title + ": " + str(data_by_title[title]))


# for element in raw_data:
    
    
# with open('data.json', 'w') as data_file:
#     json.dump(raw_data, data_file)