import json

raw_data = []
with open('recipes.json') as f:
    for line in f:
        raw_data.append(json.loads(line))

for element in raw_data:
    element.pop('author', None)
    element.pop('cook_time_minutes', None)
    element.pop('description', None)
    element.pop('error', None)
    element.pop('footnotes', None)
    element.pop('photo_url', None)
    element.pop('review_count', None)
    element.pop('time_scraped', None)
    element.pop('prep_time_minutes', None)
    element.pop('total_time_minutes', None)
    element.pop('url', None)
    
with open('data.json', 'w') as data_file:
    json.dump(raw_data, data_file)