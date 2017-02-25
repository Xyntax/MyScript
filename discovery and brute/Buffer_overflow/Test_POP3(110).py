#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xy'

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    print('\nSending evil buffer ...')
    s.connect(('192.168.20.32', 110))
    data = s.recv(1024)
    print(data)

    s.send('USER cdxy' + '\r\n')
    data = s.recv(1024)
    print(data)

    s.send('PASS test' + '\r\n')
    data = s.recv(1024)
    print(data)

    s.close()
    print('\nDone!')
except:
    print('Could not connect to POP3')
