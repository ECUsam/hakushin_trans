import json
from langdetect import detect

from null import has_kana

with open('data.json', 'r') as f:
    data = json.load(f)
with open('data2.json', 'r') as f:
    data2 = json.load(f)

num = 0
len_txt = 0
for da in data2:
    if da not in data:
        num += 1
        for txt in data2[da]['context']: len_txt+=len(txt)
        print(da, data2[da]['context'])
print(num)
print(len_txt)
all_len = 0
for da in data2:
    for txt in data2[da]["context"]: all_len+=len(txt)
print('全长：',all_len)

num = 0
fanyi = 0
no_fanyi = 0
# for da in data:
#     for txt in data[da]["context"]:
#         num += 1
#         try:
#             yuyan = detect(txt)
#         except Exception:
#             yuyan = 'ja'
#         if yuyan == 'zh-cn':
#             fanyi += len(txt)
#         else:
#             no_fanyi += len(txt)
for da in data:
    for txt in data[da]["context"]:
        num += 1
        if has_kana(txt):
            no_fanyi += len(txt)
        else:
            fanyi += len(txt)

print("总条数：", num)
print('翻译：',fanyi)
print('未翻译', no_fanyi)