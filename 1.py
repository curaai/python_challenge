def convert(ch):
    ch = ord(ch) - 97

    if 0 <= ch <= 25:
        ch = (ch + 2) % 26

    ch += 97
    return chr(ch)

if __name__ == '__main__':
    string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    conv_string = "".join([convert(x) for x in string])
    print(conv_string)
