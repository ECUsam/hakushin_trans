from file_fomater import file_function_formater
import os
import json

class All_file_ex:
    def __init__(self, filepath: str):
        assert os.path.exists(filepath)
        self.filepath = filepath
        self.dict = {}

    def exct_all(self):
        for folder, sub_folders, files in os.walk(self.filepath):
            for file in files:
                extension = os.path.splitext(file)[1]
                if extension != '.dat':
                    continue
                print(file)
                filepath = os.path.join(folder, file)
                a = file_function_formater(filepath)
                self.dict.update(a.Run())
                del a

    def get_dict(self):
        self.exct_all()
        return self.dict


# a = All_file_ex(r'E:\download\测试\新约迫真战记翻译 - 地下城 - 副本\a_default\script半翻译')
# with open('data.json', 'w') as f:
#     json.dump(a.get_dict(), f, indent=4)
#
# b = All_file_ex(r'E:\download\新約迫真戦記―ほのぼの神話ver0.41 豪華版\a_default\script_1')
# with open('data2.json', 'w') as f:
#     json.dump(b.get_dict(), f, indent=4)

a = All_file_ex(r'C:\Users\ECUsam\Documents\Tencent Files\1254281150\FileRecv\event_po5　VoiceDrama\event_po5　VoiceDrama')
with open('ないや.json', 'w') as f:
    json.dump(a.get_dict(), f, indent=4)
