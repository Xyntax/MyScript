# !/usr/bin/env python
# -*-coding:utf-8-*-
__author__ = 'xy'

name = ['Xiaoming','xiaoming','XiaoMing','Xming','xming','xMing','XM','xm']
birth = ['1995','09','9','23','199509','9509','959','19950923']

f = open('dir_s.txt','w')
for n in name:
    for b in birth:
        for b2 in birth:
            f.write(b2+n+b+'\n')
            f.write(b2+b+n+'\n')
            f.write(n+b2+b+'\n')
