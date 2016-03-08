# !/usr/bin/env python
#  -*- coding: utf-8 -*-
__author__ = 'xy'

import os
import sys
import glob

filesRead = "./file/*.csv"
file_list = glob.glob(filesRead)
ans_file = open('cat.txt', 'w')

fileobj_list = []
for each in file_list:
    fileobj_list.append(open(each, 'r').readlines())
print fileobj_list
for i in range(0, len(fileobj_list[0])):
    for each in fileobj_list:
        ans_file.write(each[i].strip() + ' ')
    ans_file.write('\n')
