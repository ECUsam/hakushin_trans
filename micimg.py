from main_ import musictran, imgtran
import re, json

def micimg(path):
    musictran(path)
    imgtran(path)


def str_dicreplace(string, jsonpath, reserve=False):
    json_ = open(jsonpath, 'r')
    diction = json.load(json_)

    if not reserve:
        for key, value in diction.items():
            key = re.split('\.', key)
            value = re.split('\.', value)
            string = string.replace(key[0], value[0])
    if reserve:
        for key, value in diction.items():
            key = re.split('\.', key)
            value = re.split('\.', value)
            string = string.replace(value[0], key[0])
    return string

def file_bgim(filepath):
    with open(filepath, 'r', encoding='utf16', errors='ignore') as f:
        naiyo = f.read()
    new_naiyo = str_dicreplace(naiyo, 'img.json')
    new_naiyo = str_dicreplace(new_naiyo, 'BGM')