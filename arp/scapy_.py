#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xy'

import logging
import subprocess
from scapy.all import *
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)


if len(sys.argv) != 2:
    print 'usage - ./scapy_.py [interface]'
    print 'example - ./scapy_.py eth0'
    print 'example will perform an ARP scan of the local subnet to which eth0 is assigned'

interface = str(sys.argv[1])

ip = subprocess.check_output("ifconfig " + interface +
                             " | grep 'inet addr' | cut -d ':' -f 2 | cut -d ' ' -f 1",
                             shell=True).strip()
prefix = ip.split('.')[0] + '.' + ip.split('.')[1] + '.' + ip.split('.')[2] + '.'

for addr in range(255):
    answer = sr1(ARP(pdst=prefix+str(addr)), timeout=0.1, verbose=0)
    if answer is None:
        pass
    else:
        print prefix + str(addr)
