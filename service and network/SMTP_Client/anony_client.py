# -*- encoding: gb2312 -*-


"""
���������ʼ�

1. helo
2. mail from
3. rcpt to
4. data
5. quit

TODO:
1 �жϷ��صĴ���.
    ��smtpЭ���У����ش�����2xx����3xx���ܼ�����һ��������4xx��5xx�ĳ�����6677
"""

import os, sys, string
import smtplib

# �ʼ���������ַ
mailserver = "smtp.163.com"
# smtp�Ự�����е�mail from��ַ
from_addr = "test@test.com"
# smtp�Ự�����е�rcpt to��ַ
to_addr = "i@cdxy.me"
# �ż�����
msg = "test mail"

svr = smtplib.SMTP(mailserver)
# ����Ϊ����ģʽ�������ڻỰ�����л��������Ϣ
svr.set_debuglevel(1)
# helo���docmd���������˻�ȡ�Է�������������Ϣ
svr.docmd("HELO server")
# mail from, �����ʼ�������
svr.docmd("MAIL FROM: <%s>" % from_addr)
# rcpt to, �ʼ�������
svr.docmd("RCPT TO: <%s>" % to_addr)
# data�����ʼ��������
svr.docmd("DATA")
# ������������
svr.send(msg)
# ������ . ��Ϊ���ķ��ͽ����ı��,��send���͵ģ�����Ҫ��getreply��ȡ������Ϣ
svr.send(" . ")
svr.getreply()
# ���ͽ������˳�
svr.quit()
