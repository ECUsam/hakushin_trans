import re, os
from changename import to_newname
import json
from baidutran import baidutrans
from diconcorl import str_dicreplace
import time
from zhconv import convert

Japanese = re.compile(
        "[０-９0-9a-z-A-Z]*[…―「（Ａ-Ｚ\u3040-\u30FF\u30A0-\u30FF\u4E00-\u9FFFぁ-んァ-ヴーｦ-ﾟ]"
        "[^@$;()=,\s]*[―\u3040-\u30FF\u30A0-\u30FF\u4E00-\u9FFFぁ-ゖァ-ヶｦ-ﾟあ-んア-ンぁ-んァ-ヴー—、。·）『』☆「」#…Ａ-Ｚ？！”“]"
    )

# TODO:写函数提取单个文件日语字符并计算长度

def excractja(file):
    with open(file, 'r', encoding='utf-16', errors='ignore') as fp:
        content = fp.read()
        allmoji = Japanese.findall(content)
        return allmoji


# TODO:遍历文件夹提取所有日语字符计算总长度


def allexcrat(folderpath):
    file_moji = []
    for foldername, subfolders, filenames in os.walk(folderpath):
        for filename in filenames:
            filepath = os.path.join(foldername, filename)
            if os.path.splitext(filepath)[1] == '.dat':
                file_moji += excractja(os.path.join(foldername, filename))
    allmoji = ''
    for moji in file_moji:
        allmoji += moji
    return allmoji


# TODO:翻译音乐、图片名称记录至字典并导回


def imgtran(path, dicname='img.json'):
    musicdic = {}
    numbers = 1
    for foldername, subfolders, filenames in os.walk(path):
        for filename in filenames:
            transname = to_newname(filename)
            musicdic[filename] = transname
            filepath = os.path.join(foldername, filename)
            newfilepath = os.path.join(foldername, transname)
            print(filename + '改名为' + transname)
            os.rename(filepath, newfilepath)
    print(musicdic)
    with open(dicname, 'w') as fb:
        json.dump(musicdic, fb)


def musictran(path, dicname='BGMdic.json'):
    musicdic = {}
    numbers = 1
    for foldername, subfolders, filenames in os.walk(path):
        for filename in filenames:
            transname = to_newname(filename)
            musicdic[filename] = transname
            filepath = os.path.join(foldername, filename)
            newfilepath = os.path.join(foldername, transname)
            while os.path.exists(newfilepath):
                basepath = os.path.splitext(newfilepath)
                part1 = basepath[0] + str(numbers)
                part2 = basepath[1]
                newfilepath = part1 + part2
                numbers += 1
            print(filename + '改名为' + transname)
            os.rename(filepath, newfilepath)
    print(musicdic)
    with open(dicname, 'w') as fb:
        json.dump(musicdic, fb)


# TODO:分组提取字符串，接入谷歌接口并进行翻译，创建字典，导入原文和翻译
# from diconcorl import subBGM
# from diconcorl import traversal

# TODO：将翻译导回到原文件


# ---------------------------------测试区域---------------------------------------------
# print(allexcrat(r'D:\APyproject\TransTest\script_success'))
# print('迫真战记的文本长度为:' + str(len(allexcrat(r'D:\APyproject\TransTest\备份\script_succeed'))))

# musictran(r'E:\download\ファッ！？レントゥーガ ver3.30b\ファッ！？レントゥーガ\a_default\bgm')

# imgtran(r'E:\download\新約迫真戦記―ほのぼの神話ver0.30 豪華版\a_default\image', 'imgdic.json')

# traversal(r'E:\download\ファッ！？レントゥーガ ver3.30b\ファッ！？レントゥーガ\a_default\script', 'BGMdic.json')
# traversal(r'D:\APyproject\TransTest\団長+αMOD\script', 'imgdic.json')



def fanyi(filepath):
    # 检测后缀
    if os.path.splitext(filepath)[1] != '.dat':
        return
    file_ = open(filepath, 'r', encoding='utf-16', errors='ignore')
    print('正在读取' + filepath)
    testjapan = file_.read()
    parrtenja = re.compile(
        #"[０-９0-9a-z-A-Z]*[…―「（Ａ-Ｚ\u3040-\u30FF\u30A0-\u30FF\u4E00-\u9FFFぁ-んァ-ヴーｦ-ﾟ][^@$;()=,\s]*[―\u3040-\u30FF\u30A0-\u30FF\u4E00-\u9FFFぁ-ゖァ-ヶｦ-ﾟあ-んア-ンぁ-んァ-ヴー—、。·）『』☆「」#…Ａ-Ｚ？！”“]"
        "[０-９0-9a-z-A-Z]*[…―「々（Ａ-Ｚ\u3040-\u30FF\u30A0-\u30FF\u4E00-\u9FFFぁ-んァ-ヴー]*[あ-んア-ン][^@$;()=,\s]*"
        "[―\u3040-\u30FF\u30A0-\u30FF\u4E00-\u9FFFぁ-ゖァ-ヶｦ-ﾟあ-んア-ンぁ-んァ-ヴー—、。· ）『』☆「」#…Ａ-Ｚ？！”“]"
    )
    tansdic = {}
    for txt in re.findall(parrtenja, testjapan):
        txt_ = str_dicreplace(txt, 'BGMdic.json', reserve=True)
        txt__ = str_dicreplace(txt_, 'imgdic.json', reserve=True)
        '''client = Translate()
        honyaku = client.translate(txt__, target='zh')
        print(honyaku.translatedText)'''
        print(txt__)
        txt___ = baidutrans(txt__)
        try:
            txt____ = convert(txt___, 'zh-cn')
        except TypeError:
            time.sleep(0.5)
            while True:
                try:
                    txt___ = baidutrans(txt__)
                    txt____ = convert(txt___, 'zh-cn')
                except TypeError:
                    continue
                break
        print(txt____)
        time.sleep(0.11)
        tansdic[txt] = txt____
    file_.close()
    for key, value in tansdic.items():
        testjapan = testjapan.replace(key, value)
    file_ = open(filepath, 'w', encoding='utf-16', errors='ignore')
    file_.write(testjapan)
    file_.close()


def allfanyi(folderpath):
    fp = open('recordEWX.json', 'r')
    record = json.load(fp)
    fp.close()
    for foldername, subfolders, filenames in os.walk(folderpath):
        for filename in filenames:
            filepath = os.path.join(foldername, filename)
            if filepath not in record:
                fanyi(filepath)
            print(filename + '翻译完成')
            record[filepath] = True
            fp = open('recordEWX.json', 'w')
            json.dump(record, fp)
            fp.close()


# allfanyi(r'E:\download\测试\汉化更新备份\a_default\script\event_po26　Genri')
# fanyi(r'E:\download\新約迫真戦記―ほのぼの神話ver0.30 豪華版\a_default\script\10_unit\Detail_retsuden.dat')


def fontchange(filepath):
    if os.path.splitext(filepath)[1] != '.dat':
        return
    file_ = open(filepath, 'r', encoding='utf-16', errors='ignore')
    print('正在读取' + filepath)
    tekst = file_.read()
    file_.close()
    event_tance = re.compile('event.*[\\s\\S]{')
    for event in re.findall(event_tance, tekst):
        tekst = tekst.replace(event, event + '\nfont(宋体,26,1)')
    file_ = open(filepath, 'w', encoding='utf-16', errors='ignore')
    file_.write(tekst)
    file_.close()
    print(os.path.basename(filepath) + '替换完成')


def allfontchange(folderpath):
    for foldername, subfolders, filenames in os.walk(folderpath):
        for filename in filenames:
            filepath = os.path.join(foldername, filename)
            fontchange(filepath)
            print(filename + '替换完成')


# allfontchange(r'E:\download\测试\汉化更新备份\a_default\script')
