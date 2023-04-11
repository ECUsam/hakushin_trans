def has_kana(text):
    kana_chars = [chr(i) for i in range(0x3040, 0x30FF + 1)]  # 平假名和片假名的 Unicode 编码范围
    for char in text:
        if char in kana_chars:
            return True
    return False


def has_4_kana(text):
    kana_chars = [chr(i) for i in range(0x3040, 0x30FF + 1)]
    num = 0
    for char in text:
        if char in kana_chars:
            num += 1
    if num >= 4:
        return True
    return False
