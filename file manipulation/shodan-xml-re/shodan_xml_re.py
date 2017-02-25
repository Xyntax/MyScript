# -*- coding: utf-8 -*-
import re
import os
"""
shodan-xml-re
将shodan导出的xml格式文件
整理成为'http://IP:PORT/'的格式
方便其他漏洞扫描工具利用

xml样本格式
</data></host><host city="Suzhou" country="CHN" ip="211.86.128.16" latitude="31.3041" longitude="120.5954" port="80" updated="03.11.2015"><data>HTTP/1.1 200 OK
Server: Resin/3.0.21
ETag: &quot;AAAATjcDeHI&quot;
Last-Modified: Tue, 31 Jul 2012 08:01:33 GMT
Content-Type: text/html
Transfer-Encoding: chunked
Date: Tue, 03 Nov 2015 02:40:48 GMT

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
            ans = "http://" + ip_port_list[0][0] + \
                ':' + ip_port_list[0][1] + '/' + '\n'
            # print ans
            file1.write(ans)
    else:
        pass
print 'over! total:' + str(num)
xml.close()
file1.close()
