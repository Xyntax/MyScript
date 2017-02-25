#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xy'


import commands

import socket
import fcntl
import struct


def arping(ip_123):
    for ip_4 in range(255):
        if 'bytes from' in commands.getoutput('arping -c 1 ' + ip_123 + '.' + str(ip_4)):
            print (ip_123 + '.' + str(ip_4))


def get_local_ip(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    inet = fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))
    ret = socket.inet_ntoa(inet[20:24])
    return ret


def get_ip_123(ipv4):
    _ip = [int(x) for x in ipv4.split('.')][:3]
    return str(_ip[0]) + '.' + str(_ip[1]) + '.' + str(_ip[2])


if __name__ == '__main__':
    print(arping(get_ip_123(get_local_ip(raw_input('wlan or eth ?')))))
