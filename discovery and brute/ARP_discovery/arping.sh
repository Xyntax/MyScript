#!/bin/bash
if["$#" -ne 1];then
    echo "Usage - ./arping.sh [interface]"
    echo "Example - ./arping.sh eth0"
    echo "Example will perform an ARP scan of local subnet to which eth0 is assigned"
    exit
fi
interface = $1
prefix = $(ifconfig $interface | grep "inet addr" | cut -d ":" -f 2 | cut -d " " -f 1 | cut -d "." -f 1-3)
for addr in $(seq 1 254 );do
    arping -c 1 $prefix.$addr | grep "bytes from" | cut -d ""-f 5 | cut -d "(" -f 2 | cut -d ")" -f 1
done
