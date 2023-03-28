import json
from openpyxl import Workbook

# 创建一个Workbook对象
workbook = Workbook()

# 获取当前活动的Worksheet对象
worksheet = workbook.active

with open('data.json', 'r') as f:
    data = json.load(f)
with open('data2.json', 'r') as f:
    data2 = json.load(f)

num_same = 0
num_not_same = 0

for key in data:
    if key not in data2:
        print(data[key]['context'])
        num_same += 1
print(num_same)