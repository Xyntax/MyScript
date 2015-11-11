# !/usr/bin/env python
#  -*- coding: utf-8 -*-
__author__ = 'xy'

import optparse


def parse_args():
    usage = """usage: %prog [options] [hostname]:port ...

            This is the Get Poetry Now! client, blocking edition.
            Run it like this:

              python get-poetry.py port1 port2 port3 ...

            If you are in the base directory of the twisted-intro package,
            you could run it like this:

              python blocking-client/get-poetry.py 10001 10002 10003

            to grab poetry from servers on ports 10001, 10002, and 10003.

            Of course, there need to be servers listening on those ports
            for that to work.
            """

    parser = optparse.OptionParser(usage)

    _, addresses = parser.parse_args()

    if not addresses:
        print parser.format_help()
        parser.exit()

    def parse_address(addr):
        if ':' not in addr:
            host = '127.0.0.1'
            port = addr
        else:
            host, port = addr.split(':', 1)

        if not port.isdigit():
            parser.error('Ports must be integers.')

        return host, int(port)

    return map(parse_address, addresses)
