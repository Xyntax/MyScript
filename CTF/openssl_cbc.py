# !/usr/bin/env python
#  -*- coding: utf-8 -*-

import base64

# def cbc(str,pos):
# val = chr(ord('X') ^ ord("'") ^ ord(cookie[pos]))
# exploit = cookie[0:pos] + val + cookie[pos + 1:]


token_base64 = 'rQFSgZI3ux7ZHqhfRXELGA=='
cipher = base64.b64decode(token_base64)


