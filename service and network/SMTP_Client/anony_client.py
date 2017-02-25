# -*- encoding: gb2312 -*-


"""
匿名发送邮件

1. helo
2. mail from
3. rcpt to
4. data
5. quit

TODO:
1 判断返回的代码.
    在smtp协议中，返回代码是2xx或者3xx才能继续下一步，返回4xx或5xx的出错了6677
"""

import os, sys, string
import smtplib

# 邮件服务器地址
mailserver = "smtp.163.com"
# smtp会话过程中的mail from地址
from_addr = "test@test.com"
# smtp会话过程中的rcpt to地址
to_addr = "i@cdxy.me"
# 信件内容
msg = "test mail"

svr = smtplib.SMTP(mailserver)
# 设置为调试模式，就是在会话过程中会有输出信息
svr.set_debuglevel(1)
# helo命令，docmd方法包括了获取对方服务器返回信息
svr.docmd("HELO server")
# mail from, 发送邮件发送者
svr.docmd("MAIL FROM: <%s>" % from_addr)
# rcpt to, 邮件接收者
svr.docmd("RCPT TO: <%s>" % to_addr)
# data命令，开始发送数据
svr.docmd("DATA")
# 发送正文数据
svr.send(msg)
# 比如以 . 作为正文发送结束的标记,用send发送的，所以要用getreply获取返回信息
svr.send(" . ")
svr.getreply()
# 发送结束，退出
svr.quit()
