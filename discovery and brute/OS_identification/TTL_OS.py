#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xy'

from scapy.all import *
import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
import sys

if len(sys.argv) != 2:
    print("Usage - ./TTL_OS.py [IP Address]")
    print("Example - ./TTL_OS.py 10.10.0.5")
    print("Example will perform ttl analysis to attempt to determine whether the system is Windows or Linux/Unix")
    sys.exit()

ip = sys.argv[1]

ans = sr1(IP(dst=str(ip)) / ICMP(), timeout=1, verbose=0)

if ans is None:
    print("No response was returned")
else:
    TTL = ans[IP].ttl
    print("TTL is :" + TTL)
    if int(TTL) <= 64:
        print("host is Linux/Unix")
    else:
        print("host is windows")
