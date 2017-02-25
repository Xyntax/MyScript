# !/usr/bin/env python
#  -*- coding: utf-8 -*-
import pycurl
import StringIO  # 这个用到里面的write函数

c = pycurl.Curl()
c.setopt(pycurl.URL, 'http://localhost:5000/c1')
b = StringIO.StringIO()
c.setopt(pycurl.WRITEFUNCTION,
         b.write)  # 把StringIO的写函数注册到pycurl的WRITEFUNCTION中，即pycurl所有获取的内容都写入到StringIO中，如果没有这一句，pycurl就会把所有的内容在默认的输出器中输出
c.setopt(pycurl.HEADERFUNCTION, b.write)
c.setopt(pycurl.FOLLOWLOCATION, 1)
c.perform()
print b.getvalue()
