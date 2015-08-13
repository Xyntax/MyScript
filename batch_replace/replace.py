#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xy'


import os
import sys
import getopt


def iterate_files(path, extension='no_ext'):

    file = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if extension == 'no_ext':
                file.append(os.path.join(root, name))
            elif name.endswith(extension):
                file.append(os.path.join(root, name))
    return file


def change_path(path, old_str, new_str, extension):

    file = iterate_files(path, extension)
    for eachfile in file:
        f = open(eachfile, 'r+')
        all_lines = f.readlines()
        f.seek(0)
        f.truncate()
        for line in all_lines:
            f.write(line.replace(old_str, new_str))
        print(eachfile + " - OK")
        f.close()


def usage():

    print('necessary:')
    print(' -i --input  -> The character to replace ')
    print(' -o --output  -> New character')

    print('unnecessary:')
    print(' -e --extension  -> Scan file with this extension')
    print(' -p --path  -> File path to scan and replace')
    print(' -h --help  -> Get help info')

    print('-----------------')
    print('sample use:')
    print(sys.argv[0] + ' -i helllo -o hello')
    print(sys.argv[0] + ' -p /home/xy/workspace -i helllo -o hello -e .txt')

    print('-----------------')
    print('create by xy 150813')
    print('connect: xyntax@163.com')

    input()
    sys.exit()


def main():

    opts, args = getopt.getopt(sys.argv[1:], "hi:o:p:e:",
                               ["help", "input=", "output=", "path=", "extension="])

    old_str, new_str, path, extension = '', '', os.getcwd(), 'no_ext'

    for op, value in opts:
        if op == '-i' or op == '--input':
            old_str = value
        elif op == '-o' or op == '--output':
            new_str = value
        elif op == '-h' or op == '--help':
            usage()
        elif op == '-p' or op == '--path':
            path = value
        elif op == '-e' or op == '--extension':
            extension = value
        else:
            print("invalid input!\n")
            usage()

    flag = True
    if not (os.path.isdir(path) or os.path.isfile(path)):
        flag = False
    if old_str == '':
        flag = False

    if flag:
        change_path(path, old_str, new_str, extension)
    else:
        print("invalid input!\n")
        usage()
