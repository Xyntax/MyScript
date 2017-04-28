# !/usr/bin/env python
#  -*- coding: utf-8 -*-
import hashlib
import random
import string

while 1:
    a = str(random.uniform(1, 100))
    m = hashlib.md5(a)
    if m.hexdigest().startswith('749e3e'):
        print(a)
        break
