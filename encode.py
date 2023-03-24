import shutil

import chardet
import os

class encode_changer:
    def __init__(self, path, isFloder=False):
        self.isFloder = isFloder
        if self.isFloder:
            self.floderpath = path
        else:
            self.filepath = path

    def get_encoding(self):
        # 二进制方式读取，获取字节数据，检测类型
        with open(self.filepath, 'rb') as f:
            return chardet.detect(f.read())['encoding']

    def change_encode(self):
        with open(self.filepath, 'rb+') as fp:
            content = fp.read()
            encoding = self.get_encoding()
            # 我是大傻逼 or encoding == 'CP932'
            if encoding is None or encoding == 'Windows-1254':
                encoding = 'shift_jis'
                print(encoding)
                content = content.decode(encoding, errors='ignore').encode('utf-16', errors='ignore')
                fp.seek(0)
                fp.write(content)
                return
            print(encoding)
            content = content.decode(encoding, errors='ignore').encode('utf-16', errors='ignore')
            fp.seek(0)
            fp.write(content)

    def change_all(self, source_path):
        # 备份文件
        number = 1
        while True:
            target_name = os.path.basename(source_path) + '_' + str(number)
            if not os.path.exists(target_name):
                break
            number = number + 1
        target_path = os.path.join(os.path.split(source_path)[0], target_name)
        source_path = os.path.abspath(source_path)
        target_path = os.path.abspath(target_path)
        shutil.copytree(source_path, target_path)
        filepath = target_path
        # 开始遍历
        for foldername, subfolders, filenames in os.walk(filepath):
            for filename in filenames:
                extension = os.path.splitext(filename)[1]
                if extension == '.dat':
                    print(str(foldername) + ' ' + str(filename))
                    self.change_encode()