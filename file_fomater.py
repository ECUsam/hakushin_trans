import re
import logging
from io import StringIO
from main import Stack

logging.basicConfig(level=logging.DEBUG, filename='myapp.log', filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s')


class file_function_formater:
    def __init__(self, filepath: str, language='jp'):
        try:
            self.file = open(filepath, 'r', encoding='utf16', errors='ignore')
        except Exception:
            print('打开文件失败')
        self.language = language
        if self.language == 'jp':
            self.parrtenja = re.compile(
                "[０-９0-9a-z-A-Z]*[…―「（Ａ-Ｚ\u3040-\u30FF\u30A0-\u30FF\u4E00-\u9FFFぁ-んァ-ヴーｦ-ﾟ][^@$;()=,"
                "\s]*[―\u3040-\u30FF\u30A0-\u30FF\u4E00-\u9FFFぁ-ゖァ-ヶｦ-ﾟあ-んア-ンぁ-んァ-ヴー—、。·）『』☆「」#…Ａ-Ｚ？！”“]")
        self.function_list = ['event', 'class', 'unit', 'story', 'scenario', 'spot', 'detail', 'skill']
        self.dict = {}
        # 原本还有[的但是我翻译的时候瞎写导致括号不平衡
        # 追伸：(也让我乱搞没了，白写了这里
        # 再追伸：(不对的地方手动改了
        self.kako = ['{']
        self.kako2 = ['}']
        self.stack = Stack()
        self.bgm_img_font_func = ['playBGM(', 'font(', 'bcg =', 'bcg=', 'bgm =', 'battle_bgm =', 'world_bgm =', 'bg(']
        self.res_dict = {}
        # 遍历的时候不让用file.tell，我恨你python
        self.offset = 0

    def __del__(self):
        self.file.close()

    def find_function(self, line: str):
        func_parten = re.compile("(" + '|'.join(self.function_list) + ")" + '\s+([^{]+)')
        if re.match(func_parten, line):
            fech = re.match(func_parten, line)
            res = fech.group(2).split(':')[0]
            func_type = fech.group(1)
            full_res = fech.group()
            offset = (len(line) + 1 - (line.index(full_res) + len(full_res))) * 2
            # print(len(line), line.index(full_res), len(full_res))
            # print(res, full_res, offset, self.offset)
            return [func_type, res.strip(), full_res, offset]
        return False

    def find_function_pointer(self):
        res = ''
        for line in self.file:
            print(self.offset)
            # 换行占了4个bit它只给算2个bit
            self.offset += (len(line) + 1) * 2
            if line[:2] == '//':
                continue
            res = self.find_function(line)
            if res:
                break
        return res

    def fetch_function(self, offset=0) -> str:
        func = ''
        self.offset = self.offset - offset
        self.file.seek(self.offset)
        tmp = self.file.read(1)
        self.offset += 2

        while tmp != '{':
            # print(tmp, end='')
            tmp = self.file.read(1)
            self.offset += 2
        func += tmp
        assert tmp in self.kako
        self.stack.push(tmp)
        while not self.stack.is_empty():
            tmp = self.__read_one()
            func += tmp
            if tmp in self.kako:
                self.stack.push(tmp)
            if tmp in self.kako2:
                # print(self.offset, tmp, self.kako2.index(tmp), self.kako.index(self.stack.peek()))
                assert self.kako2.index(tmp) == self.kako.index(self.stack.peek()), self.offset
                self.stack.pop()
            print(func)
        return func

    def get_func_list(self):
        while True:
            res = self.find_function_pointer()

            if not res:
                break
            func = self.fetch_function(res[3])
            self.dict[res[1]] = {'type': res[0], 'full_name': res[2], 'context': func}

    def __read_one(self) -> str:
        print(self.offset)
        tmp = self.file.read(1)
        if tmp == '\n':
            self.offset += 4
        else:
            self.offset += 2

        return tmp

    def out_of_bgm(self):
        for key, value in self.dict.items():
            res = ''
            f = StringIO(value["context"])
            for line in f:
                ifnotin = True
                for no in self.bgm_img_font_func:
                    if no in line:
                        ifnotin = False
                if '//' in line: line = line.split('//')[0]
                if ifnotin: res += line
            self.dict[key]["context"] = res

    def turn_to_text(self):
        for key, value in self.dict.items():
            res = re.findall(self.parrtenja, value["context"])
            if res:
                value["context"] = res
                self.res_dict[key] = value
                # print(key, value)

    def Run(self):
        self.get_func_list()
        self.out_of_bgm()
        self.turn_to_text()
        return self.res_dict


a = file_function_formater('00_簡易戦闘.dat')
a.Run()
