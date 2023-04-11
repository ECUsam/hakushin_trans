from file_fomater import file_function_formater
import json
import os

class replacer(file_function_formater):

    def __init__(self, filepath: str):
        super().__init__(filepath)
        self.naiyo = self.file.read()
        self.file.seek(0)
        with open('jifan_trans_naiya.json', 'r', encoding='utf16') as f:
            self.trans = json.load(f)

    def print_dict(self):
        print(self.dict)

    def check_dict(self):
        for da in self.dict:
            print(self.dict[da]['context'])

    def replace(self):
        for key in self.dict:
            if key not in self.trans:
                continue
            if self.trans[key]['iftrans']:
                tranres = self.dict[key]['context']
                for key_ in sorted(self.trans[key]['trans'], key=len, reverse=True):
                    value = self.trans[key]['trans'][key_]
                    after = tranres.replace(key_, value)
                    tranres = after
                tihuan = self.naiyo.replace(self.dict[key]['context'], tranres, 1)
                self.naiyo = tihuan

        file_ = open(self.filepath, 'w', encoding='utf-16', errors='ignore')
        file_.write(self.naiyo)
        file_.close()


def all_replace(foler_path):
    for folder, sub_folders, files in os.walk(foler_path):
        for file in files:
            extension = os.path.splitext(file)[1]
            if extension != '.dat':
                continue
            print(file)
            filepath = os.path.join(folder, file)
            n = replacer(filepath)
            n.get_func_list()
            n.replace()


all_replace('script_1')
