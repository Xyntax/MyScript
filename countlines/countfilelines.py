#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xy'

import os
import os.path
import sys
import getopt

class CountFileLines(object):
    total_lines = 0

    def count(self, rootpath, extension):
        if os.path.isdir(rootpath):
            rootfiles = os.listdir(rootpath)
            for each in rootfiles:
                full_path = os.path.join(rootpath, each)
                if os.path.isdir(full_path):
                    self.count(full_path, extension)
                else:

                    if os.path.isfile(full_path):
                        if extension in each or extension == '':
                            fobj = open(full_path, 'r')
                            lines = len(fobj.readlines())
                            self.total_lines += lines
                            print full_path + "\n" + str(lines)
                    else:
                        print each + ': not a file'


path = ''
extension = ''
opts, args = getopt.getopt(sys.argv[1:], "hp:e:")
if opts == '':
    path = os.getcwd()
else:
    for op, value in opts:
        if op == '-p':
            path = value
        if op == '-e':
            extension = value

a = CountFileLines()
a.count(path, extension)
print '\ntotal lines:\n' + str(a.total_lines)
