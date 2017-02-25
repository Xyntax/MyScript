#!/usr/bin/python
__author__ = 'xy'

import logging
import sys

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy import *

if len(sys.argv) != 2:
    print('Usage - ./arp_file.py [interface]')
    print('Example - ./arp_file.py eth0')
    print('Example will perform an ARP scan of the local subnet ro which eth0 is assigned')
    sys.exit()

filename = str(sys.argv[1])
file = open(filename, 'r')

for addr in file:
    answer = sr1(ARP(pdst=addr.strip()), timeout=0.1, verbose=0)
    if not answer:
        pass
    else:
        print addr.strip()
