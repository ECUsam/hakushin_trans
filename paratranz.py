import json
import os

def has_kana(text):
    kana_chars = [chr(i) for i in range(0x3040, 0x30FF + 1)]  # 平假名和片假名的 Unicode 编码范围
    for char in text:
        if char in kana_chars:
            return True
    return False

with open('data.json', 'r') as f:
    data = json.load(f)
with open('data2.json', 'r') as f:
    data2 = json.load(f)

paratranz = []
function_list = ['event', 'class', 'unit', 'story', 'scenario', 'spot', 'detail', 'skill', 'race', 'power', 'movetype', 'voice']
lists = {}
for func in function_list:
    lists[func] = []

for da in data2:
    if da in data:
        if len(data2[da]['context']) == len(data[da]['context']):
            data2[da]["trans"] = data[da]['context']
        else:
            data2[da]["trans"] = ""
    else:
        data2[da]["trans"] = ""


for da in data2:
    for i in range(len(data2[da]['context'])):
        try:
            trans = data2[da]['trans'][i]
            if has_kana(trans):
                print(trans)
                trans = ''
        except IndexError:
            trans = ''

        tiaomu = {
            "key": da + '_' + str(i),
            "original": data2[da]['context'][i],
            "translation": trans,
            "context": '类型：' + data2[da]['type'] + '.文件：' + data2[da]['repath']
        }
        func = data2[da]['type']
        my_list = lists[func]
        my_list.append(tiaomu)

with open('paratranz.json', 'w', encoding='utf16') as para:
    json.dump(paratranz, para, indent=4, ensure_ascii=False)

directory = './fanyi'
if not os.path.exists(directory):
    os.makedirs(directory)

for func in lists:
    with open('.\\fanyi\\'+func+'.json', 'w', encoding='utf16') as f:
        json.dump(lists[func], f, indent=4, ensure_ascii=False)
