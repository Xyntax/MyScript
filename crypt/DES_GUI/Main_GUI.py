#!/usr/bin/python
# -*- coding: UTF-8 -*-

from pyDes import *  # for DES
from Tkinter import *  # for GUI
import tkFileDialog  # for open file
import os  # for getcwd()

__author__ = 'xy'


def on_click_openfile():
    # 打开文件
    filename = tkFileDialog.askopenfilename(initialdir=os.getcwd())  # 系统中选择文件
    # print filename
    f = open(filename)
    global data
    data = f.read()  # 读文件内容


def on_click_en():
    # 设置密钥
    key = text.get()
    # print key
    if key == '':
        # print 'use default key: 13281166'
        k = des("13281166")  # 设置default密钥13281166
    else:
        k = des(key)  # 初始化des设置
    d = k.encrypt(data, "*")  # 加密

    filepath = os.getcwd() + '\cipher_text'
    cipher_file = open(filepath, 'w')
    cipher_file.write(d)
    label2['text'] = '加密完成!' + '\n' + '密文文件请查看：' + '\n' + filepath + '\n'


def on_click_de():
    # 设置密钥
    key = text.get()
    # print key
    if key == '':
        # print 'use default key: 13281166'
        k = des("13281166")  # 设置default密钥13281166
    else:
        k = des(key)  # 初始化des设置
    p = k.decrypt(data, "*")  # 解密

    filepath = os.getcwd() + '\plain_text.txt'
    cipher_file = open(filepath, 'w')
    cipher_file.write(p)
    label2['text'] = '解密完成!' + '\n' + '明文文件请查看：' + '\n' + filepath + '\n'


if __name__ == '__main__':
    root = Tk(className='DES加解密程序 by xy13281166')

    label1 = Label(root)
    label1['text'] = 'DESenc/dec_GUI\n\n edit by xy 13281166\n at 151014\n\nUsage:\n 1.输入8位密钥 ' \
                     '(默认为：13281166) \n 2.选择需要加解密的文件\n 3.点击按钮进行加解密操作\n'
    label1.pack()

    label2 = Label(root)
    label2['text'] = '请输入密钥(8位)'
    label2.pack()

    text = StringVar()
    text.set('13281166')

    entry = Entry(root)
    entry['textvariable'] = text
    entry.pack()

    button1 = Button(root)
    button1['text'] = '打开文件'
    button1['command'] = on_click_openfile
    button1.pack()

    button2 = Button(root)
    button2['text'] = '加密该文件'
    button2['command'] = on_click_en
    button2.pack()

    button3 = Button(root)
    button3['text'] = '解密该文件'
    button3['command'] = on_click_de
    button3.pack()

    root.mainloop()

# data = "String to Pad".encode('ascii')
# # set key
# k = des("13281166")
# # encrypt data
# d = k.encrypt(data, "*")
# print d
# plaintext = k.decrypt(d, '*')
# print plaintext
# if plaintext != data:
#     print ("Test:  Error: decrypt does not match. %r != %r" % (data, plaintext))
# else:
#     print ("Test:  Successful")
