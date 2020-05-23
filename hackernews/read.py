import json

with open('items.json') as jsonfile:
    item = json.load(jsonfile)

for p in item['posts']:
    print(p['title'])
    print(p['link'])
    print()

