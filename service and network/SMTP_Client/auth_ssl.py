# -*- encoding: gb2312 -*-

"""
ͨ��SSL�����ʼ�

 ������starttls�����smtplib.starttls()��
 �������е��ʼ�ϵͳ��֧�ְ�ȫ�ʼ��ģ������Ҫ��ehlo�ķ���ֵ����ȷ�ϣ����������starttls���ű�ʾ֧�֡�

TODO:
1 �жϷ��صĴ���.
    ��smtpЭ���У����ش�����2xx����3xx���ܼ�����һ��������4xx��5xx�ĳ�����
"""

import os, sys, string
import smtplib
import base64

# �ʼ���������ַ
mailserver = "smtp.163.com"
# �ʼ��û���
username = "xyntax@163.com"
# ����
password = raw_input("pass > ")
# smtp�Ự�����е�mail from��ַ
from_addr = "xyntax@163.com"
# smtp�Ự�����е�rcpt to��ַ
to_addr = "i@cdxy.me"
# �ż�����
msg = "my test mail"

svr = smtplib.SMTP(mailserver)
# ����Ϊ����ģʽ�������ڻỰ�����л��������Ϣ
svr.set_debuglevel(1)
# ehlo���docmd���������˻�ȡ�Է�������������Ϣ�����֧�ְ�ȫ�ʼ�������ֵ�����starttls��ʾ
svr.docmd("EHLO server")
svr.starttls()  # <------ ���о����¼ӵ�֧�ְ�ȫ�ʼ��Ĵ��룡
# auth login ����
svr.docmd("AUTH LOGIN")
# �����û�������base64������ģ���send���͵ģ�����Ҫ��getreply��ȡ������Ϣ
svr.send(base64.encodestring(username))
svr.getreply()
# ��������
svr.send(base64.encodestring(password))
svr.getreply()
# mail from, �����ʼ�������
svr.docmd("MAIL FROM: <%s>" % from_addr)
# rcpt to, �ʼ�������
svr.docmd("RCPT TO: <%s>" % to_addr)
# data�����ʼ��������
svr.docmd("DATA")
# ������������
svr.send(msg)
# ������ . ��Ϊ���ķ��ͽ����ı��
svr.send(" . ")
svr.getreply()
# ���ͽ������˳�
svr.quit()
