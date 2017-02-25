# !/usr/bin/env python
#  -*- coding: utf-8 -*-
import marshal
import base64


def foo():
    import os
    def ppp(s):
        os.system('id')
        print s
    ppp('hello')


# print base64.b64encode(marshal.dumps(foo.func_code))

# marshal.loads(base64.b64decode(
#     'YwAAAAABAAAAAgAAAEMAAABzHQAAAGQBAGQAAGwAAH0AAHwAAGoBAGQCAIMBAAFkAABTKAMAAABOaf////90AgAAAGlkKAIAAAB0AgAAAG9zdAYAAABzeXN0ZW0oAQAAAFIBAAAAKAAAAAAoAAAAAHM5AAAAL2hvbWUveHkvdGVzdHNwYWNlL1NTVElfZGVtby9zZXJpYWxpemF0aW9uL21hcnNoYWwtZXhwLnB5dAMAAABmb28HAAAAcwQAAAAAAQwB'))


a = marshal.dumps(foo.func_code)
print marshal.loads(a)
