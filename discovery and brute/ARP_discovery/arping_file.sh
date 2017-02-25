#!/bin/bash
if [ "$#" -ne 1 ]; then
    echo "Usage - ./arping_file.sh [interface]"
    echo "Example - ./arping_file.sh eth0"
    echo "Example will perform an ARP scan of the local subnet tp whicj eth0 is assigned"
fi
file = $1
for addr in $(cat $file); do
    arping -c 1 $addr | grep "bytes from" | cut -d " " -f 5 | cut -d "(" -f 2 | cut -d ")" -f 1
done 
