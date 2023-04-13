import json
import os
from null import has_4_kana
import re

fenge = re.compile('[#@$]')

with open('raw_trans_2.json', 'r', encoding='utf16') as f:
    raw_trans = json.load(f)

paratranz = []
function_list = ['event', 'class', 'unit', 'story', 'scenario', 'spot', 'detail', 'skill', 'race', 'power', 'movetype', 'voice']
lists = {}
for func in function_list:
    lists[func] = []


for da in raw_trans:
    for i in range(len(raw_trans[da]['context'])):
        original = raw_trans[da]['context'][i]
        if raw_trans[da]['iftrans']:
            if original not in raw_trans[da]['trans']:print(da)
            trans = raw_trans[da]['trans'][original]
            if has_4_kana(trans): trans = ''
        else:
            trans = ''
        tiaomu = {
            "key": da + '@_' + str(i) + '@_0',
            "original": original,
            "translation": trans,
            "context": '类型：' + raw_trans[da]['type'] + '.文件：' + raw_trans[da]['repath']
        }

        if trans == '':

            ori_yuan = re.split(fenge, original)
            for j in range(len(ori_yuan)):
                tiaomu = {
                    "key": da + '@_' + str(i) + '@_'+ str(j),
                    "original": ori_yuan[j],
                    "translation": trans,
                    "context": '类型：' + raw_trans[da]['type'] + '.文件：' + raw_trans[da]['repath']
                }
                func = raw_trans[da]['type']
                my_list = lists[func]
                my_list.append(tiaomu)
            continue

        func = raw_trans[da]['type']
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
