import json

with open('naiya.json', 'r') as f:
    naiya = json.load(f)
with open('jifan_trans.json', 'r', encoding='utf16') as f:
    jifan = json.load(f)

for da in naiya:
    if da in jifan and da is not None:
        jifan[da]['iftrans'] = True
        trans = {key: value for key, value in zip(jifan[da]['context'], naiya[da]['context'])}
        jifan[da]['trans'] = trans


with open('jifan_trans_naiya.json', 'w', encoding='utf16') as f:
    json.dump(jifan, f, indent=4, ensure_ascii=False)
