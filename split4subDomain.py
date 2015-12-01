import re
import os
import sys
filepath = sys.argv[1]
print("opening " + filepath)
file = open('./'+filepath,'r')
file1 = open('./'+filepath + '_URL','w')
file2 = open('./'+filepath + '_IP','w')
text_list = file.readlines()
file.close()
# print text_list
url_list=[]
ip_list=[]
for line in text_list:
    url,ip=line.split('\t')

    if url not in url_list:
        url_list.append(url)
        file1.write('http://' + url + '\n')
    if ip not in ip_list:
        if ', ' in ip:
            ip_=ip.split(', ')
            for each in ip_:
                if each not in ip_list:
                    ip_list.append(each)
                    file2.write(each + '\n')
                else:
                    pass
        else:
            ip_list.append(ip)
            file2.write(ip + '\n')

file1.close()
file2.close()
#
