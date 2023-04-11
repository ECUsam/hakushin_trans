import json
import concurrent.futures
from baidutran import baidutrans
from null import has_4_kana

with open('raw_trans.json', 'r', encoding='utf-16') as f:
    raw_trans = json.load(f)

cache = {}


def translate(txt):
    if txt in cache:
        return cache[txt]
    else:
        while True:
            result = baidutrans(txt)
            if result is not None:
                print(result)
                return result


def process_item(key):
    if not raw_trans[key]['iftrans']:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            trans = list(executor.map(translate, raw_trans[key]['context']))
        trans_dict = {key: value for key, value in zip(raw_trans[key]['context'], trans)}
        raw_trans[key]['iftrans'] = True
        raw_trans[key]['trans'] = trans_dict
    else:
        raw_dict = raw_trans[key]['trans']
        for key_trans, value in raw_dict.items():
            if has_4_kana(value):
                jifan_ = translate(value)
                raw_trans[key]['trans'][key_trans] = jifan_


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(process_item, raw_trans.keys())

with open('jifan_trans.json', 'w', encoding='utf-16') as f:
    json.dump(raw_trans, f, indent=4, ensure_ascii=False)
