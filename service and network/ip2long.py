# !/usr/bin/env python
#  -*- coding: utf-8 -*-
from socket import inet_aton
from struct import unpack


def ip2long(ip_addr):
    return unpack("!L", inet_aton(ip_addr))[0]


print inet_aton('1945096731')
print ip2long('1945096731')
print ip2long('115.15716891')
print ip2long('115.239.53787')
print ip2long('0x73.0x000EFD21B')
print ip2long('0x73.15716891')
print ip2long('0163.0xEFD21B')

from socket import inet_aton
from struct import unpack


def ip2long(ip_addr):
    return unpack("!L", inet_aton(ip_addr))[0]


def is_inner_ipaddress(ip):
    ip = ip2long(ip)
    return ip2long('127.0.0.0') >> 24 == ip >> 24 or \
           ip2long('10.0.0.0') >> 24 == ip >> 24 or \
           ip2long('172.16.0.0') >> 20 == ip >> 20 or \
           ip2long('192.168.0.0') >> 16 == ip >> 16
