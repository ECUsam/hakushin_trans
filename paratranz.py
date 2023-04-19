import json
import os

from baidutran import baidutrans
from null import has_4_kana
import re


def filenamer(input_str):
    valid_str = re.sub(r'[^\w\-. ]', '', input_str)  # 只保留英文、数字、下划线、连字符、点、空格
    valid_str = re.sub(r'[\s]+', ' ', valid_str)  # 将连续的空格替换为单个空格
    valid_str = valid_str.replace(' ', '_')  # 将空格替换为下划线
    return valid_str


fenge = re.compile('[#@$]')

with open('raw_trans_3.json', 'r', encoding='utf16') as f:
    raw_trans = json.load(f)

function_list = ['event', 'class', 'unit', 'story', 'scenario', 'spot', 'detail', 'skill', 'race', 'power', 'movetype',
                 'voice']
lists = {}
# for func in function_list:
#     lists[func] = []


for da in raw_trans:
    file_path = raw_trans[da]['repath']
    if file_path not in lists:
        lists[file_path] = []
    for i in range(len(raw_trans[da]['context'])):
        original = raw_trans[da]['context'][i]
        if raw_trans[da]['iftrans']:
            if original not in raw_trans[da]['trans']: print(da)
            trans = raw_trans[da]['trans'][original]
            if has_4_kana(trans): trans = ''
        else:
            trans = ''
        tiaomu = {
            "key": da + '@_' + str(i) + '',
            "original": original,
            "translation": trans,
            "context": '类型：' + raw_trans[da]['type'] + '.文件：' + raw_trans[da]['repath']
        }

        # if trans == '':
        #
        #     ori_yuan = re.split(fenge, original)
        #     for j in range(len(ori_yuan)):
        #         tiaomu = {
        #             "key": da + '@_' + str(i) + '@_'+ str(j),
        #             "original": ori_yuan[j],
        #             "translation": trans,
        #             "context": '类型：' + raw_trans[da]['type'] + '.文件：' + raw_trans[da]['repath']
        #         }
        #         func = raw_trans[da]['repath']
        #         my_list = lists[func]
        #         my_list.append(tiaomu)
        #     continue

        func = raw_trans[da]['repath']
        my_list = lists[func]
        my_list.append(tiaomu)

with open('name.json', 'r', encoding='utf16') as f:
    name_dict = json.load(f)

for func in lists:
    dir_path = os.path.dirname(func)
    file_dire = func.split('.dat')[0]
    filename_base = os.path.basename(func).split('.dat')[0]
    if filename_base not in name_dict:
        filename_new = baidutrans(filename_base, toLang='en')
        filename_new = filenamer(filename_new)
        name_dict[filename_base] = filename_new
    else:
        filename_new = name_dict[filename_base]

    print(filename_new)
    file_dire = file_dire.replace(filename_base, filename_new)

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    with open(file_dire + '.json', 'w', encoding='utf16') as f:
        json.dump(lists[func], f, indent=4, ensure_ascii=False)

with open('name.json', 'w', encoding='utf16') as f:
    json.dump(name_dict, f, indent=4, ensure_ascii=False)
