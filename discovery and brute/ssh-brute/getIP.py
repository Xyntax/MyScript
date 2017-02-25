# -*- coding: utf-8 -*-
import re
import os
"""
返回IP列表
"""

filename = raw_input("filename >")
xml = open(filename, 'r')
file1 = open(filename + '_sorted', 'w')
reg = r'ip="(.*?)".*?port="(.*?)"'
num = 0
for each in xml.readlines():
    ip_port_list = re.findall(reg, each)
    if ip_port_list:
        if len(ip_port_list) > 1:
            print "匹配到多个IP:port! 请检查xml文件"
            exit
        else:
            num += 1
            ans = ip_port_list[0][0] + '\n'
            # print ans
            file1.write(ans)
    else:
        pass
print 'over! total:' + str(num)
xml.close()
file1.close()
