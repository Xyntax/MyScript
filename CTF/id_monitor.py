# !/usr/bin/env python
#  -*- coding: utf-8 -*-
import requests
import re


def get(i):
    c = {'PHPSESSID': '99cue0tq11kpo0fm0fof4k2001'}
    r = requests.get(url='http://52.80.19.55/user.php/' + str(i), cookies=c)
    s = re.findall('Your study vow:(.*?)Your final exam grades:(.*?)', r.content)
    print(s)


for i in range(100):
    get(i)
