import json

with open('naiya.json', 'r') as f:
    naiya = json.load(f)
with open('data.json', 'r') as f:
    data = json.load(f)

for da in naiya:
    if da in data:
        data[da]['context'] = naiya[da]['context']
    else:
        print(da)

with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)
