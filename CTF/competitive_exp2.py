# !/usr/bin/env python
#  -*- coding: utf-8 -*-
import requests
import threading
import time
import re
from bs4 import BeautifulSoup

DEBUG = True

HOST = 'http://218.2.197.235:23739'
PROCESS = HOST + '/process.php'
ACTION = HOST + '/action.php'
HOME = HOST + '/home.php'
HISTORY = HOST + '/history.php'
REFOUND = HOST + '/refund.php'

COOKIE = {
    'PHPSESSID': 'dbf94f58487df0f6ace9d9b8dcaadda3'
}

DATA1 = {'comment': '1',
         'money': '1',
         'point': '1',
         'mypoint': '499',
         'mymoney': '1'
         }
DATA2 = {u'comment': u'1', u'mymoney': u'1', u'point': u'1', u'money': u'1',
         u'sign': u'60515349bea2559b7a971e8d484682ba', u'mypoint': u'499'}

lock1 = threading.Lock()
lock2 = threading.Lock()


def _get_static_post_attr(page_content):
    """
    拿到<input type='hidden'>的post参数，并return
    """
    _dict = {}
    soup = BeautifulSoup(page_content, "html.parser")
    for each in soup.find_all('input'):
        if 'value' in each.attrs and 'name' in each.attrs:
            _dict[each['name']] = each['value']
    return _dict


def get_current_money():
    r3 = requests.get(HOME, cookies=COOKIE)
    print re.findall('name="mypoint" value="(\w+)"', r3.content)


def exchange():
    # lock1.acquire()
    while 1:
        try:
            r = requests.post(url=PROCESS, data=DATA1, cookies=COOKIE)
            if 'action="action.php"' not in r.content:
                exit(r.content)
            # print(data2)
            r2 = requests.post(url=ACTION, data=DATA2, cookies=COOKIE)
            if 'Succeed' not in r2.content:
                exit(r2.content)
            get_current_money()
        except:
            pass
            # lock1.release()


def refound():
    # lock2.acquire()
    while 1:
        try:
            r = requests.get(HISTORY, cookies=COOKIE)
            href = re.findall("<a href='(.*?)'", r.content)
            if href:
                url = HOST + '/' + href[0]
                r2 = requests.get(url, cookies=COOKIE)
                data = _get_static_post_attr(r2.content)
                r3 = requests.post(REFOUND, data=data, cookies=COOKIE)
                if 'Succeed' not in r3.content:
                    exit(r3.content)
        except:
            pass
            # lock2.release()


def main():
    for i in range(5):
        t1 = threading.Thread(target=exchange)
        t1.start()
        t2 = threading.Thread(target=refound)
        t2.start()


    time.sleep(10)

main()
