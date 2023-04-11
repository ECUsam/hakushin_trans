import json

with open('data.json', 'r') as f:
    data = json.load(f)
with open('data2.json', 'r') as f:
    data2 = json.load(f)

for da in data2:
    if da in data and da is not None:
        data2[da]['iftrans'] = True
        trans = {key: value for key, value in zip(data2[da]['context'], data[da]['context'])}
        data2[da]['trans'] = trans
    else:
        data2[da]['iftrans'] = False

with open('raw_trans.json', 'w', encoding='utf16') as f:
    json.dump(data2, f, indent=4, ensure_ascii=False)
