import json
from baidutran import baidutrans
from null import has_4_kana
with open('raw_trans.json', 'r', encoding='utf16') as f:
    raw_trans = json.load(f)

for key in raw_trans:
    if not raw_trans[key]['iftrans']:
        trans = []
        for txt in raw_trans[key]['context']:
            jifan = baidutrans(txt)
            print(jifan)
            trans.append(jifan)
        trans_dict = {key: value for key, value in zip(raw_trans[key]['context'], trans)}
        raw_trans[key]['iftrans'] = True
        raw_trans[key]['trans'] = trans_dict

    else:
        raw_dict = raw_trans[key]['trans']
        for key_trans, value in raw_dict.items():
            if has_4_kana(value):
                jifan_ = baidutrans(value)
                print(jifan_)
                raw_trans[key]['trans'][key_trans] = jifan_

with open('jifan_trans.json', 'w', encoding='utf16') as f:
    json.dump(raw_trans, f, indent=4, ensure_ascii=False)