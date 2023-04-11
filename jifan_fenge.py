import re
from baidutran import baidutrans

def jifan_fenge(fulltext):
    parrtenja = re.compile(
        "[０-９0-9a-z-A-Z]*[…―「々（Ａ-Ｚ\u3040-\u30FF\u30A0-\u30FF\u4E00-\u9FFFぁ-んァ-ヴー]*[あ-んア-ン][^@$;()=,\s]*"
        "[―\u3040-\u30FF\u30A0-\u30FF\u4E00-\u9FFFぁ-ゖァ-ヶｦ-ﾟあ-んア-ンぁ-んァ-ヴー—、。· ）『』☆「」#…Ａ-Ｚ？！”“]"
    )
    res = fulltext
    for txt in re.findall(parrtenja, fulltext):
        txt_jifan = baidutrans(txt)
        res = res.replace(txt, txt_jifan)
    print(res)
    return res
