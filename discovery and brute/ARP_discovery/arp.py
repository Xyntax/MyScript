#!/usr/bin/python
__author__ = 'xy'

import logging
import subprocess
import sys

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy import *

if len(sys.argv) != 2:
    print('Usage - ./arp.py [interface]')
    print('Example - ./arp.py eth0')
    print('Example will perform an ARP scan of the local subnet ro which eth0 is assigned')
    sys.exit()

interface = str(sys.argv[1])

ip = subprocess.check_output("ifconfig " + interface + " | grep 'inet addr' | cut -d ':' -f 2 | cut -d ' ' -f 1",
                             shell=True).strip()
prefix = ip.split('.')[0] + '.' + ip.split('.')[1] + '.' + ip.split('.')[2] + '.'

for addr in range(0, 254):
    answer = sr1(ARP(pdst=prefix + str(addr)), timeout=0.1, verbose=0)
    if not answer:
        pass
    else:
        print (prefix + str(addr))
