import os, re
from baidutran import baidutrans

# client = Translate()
script_path = r'E:\download\新約迫真戦記―ほのぼの神話ver0.41 豪華版\a_default\script'
onlyzimu = re.compile('[a-zA-Z]?[0-9]?_?|\.')


def enchange(script_path):
    changename(script_path)


def to_newname(name):
    engnamelist = onlyzimu.findall(name)
    _name = ''
    for taname in engnamelist:
        _name += taname
    if _name == name:
        return name

    namelist = re.split('\.', name)
    # honyaku = client.translate(namelist[0], target='en')
    honyaku = baidutrans(namelist[0], toLang='en')
    newname = onlyzimu.findall(honyaku)
    realname = ''
    for alber in newname:
        realname += alber
    if len(namelist) >= 2:
        realname += '.' + namelist[1]
    return realname


def changename(path):
    for foldername, subfolders, filenames in os.walk(path):
        print('当前文件夹' + foldername)
        fonewname = to_newname(os.path.basename(foldername))

        for filename in filenames:
            print('文件为' + filename)

            realname = to_newname(filename)
            filepath = os.path.join(script_path, foldername, filename)
            dirname = os.path.split(filepath)
            realnamepath = os.path.join(dirname[0], foldername, realname)
            os.rename(filepath, realnamepath)
            print('已改名为' + os.path.basename(realnamepath))

        folderpath = os.path.join(script_path, foldername)
        dirfoldername = os.path.split(folderpath)
        newfolderpath = os.path.join(dirfoldername[0], fonewname)
        print('新路径' + newfolderpath)
        os.rename(folderpath, newfolderpath)
        print('文件夹已改名为' + os.path.basename(newfolderpath))


# enchange(script_path)
