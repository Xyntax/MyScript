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

    # _ = <Values at 0x7f6e5f76d488: {}>
    # address = ['111', '222', '333']
    addresses = parser.parse_args()[1]
    # print(addresses)
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

    # return [('127.0.0.1', 111), ('127.0.0.1', 222), ('127.0.0.1', 333)]
    return map(parse_address, addresses)

# print(parse_args())
