# -*- encoding: gb2312 -*-

"""
通过SSL发送邮件

 增加了starttls的命令，smtplib.starttls()。
 不是所有的邮件系统都支持安全邮件的，这个需要从ehlo的返回值里来确认，如果里面有starttls，才表示支持。

TODO:
1 判断返回的代码.
    在smtp协议中，返回代码是2xx或者3xx才能继续下一步，返回4xx或5xx的出错了
"""

import os, sys, string
import smtplib
import base64

# 邮件服务器地址
mailserver = "smtp.163.com"
# 邮件用户名
username = "xyntax@163.com"
# 密码
password = raw_input("pass > ")
# smtp会话过程中的mail from地址
from_addr = "xyntax@163.com"
# smtp会话过程中的rcpt to地址
to_addr = "i@cdxy.me"
# 信件内容
msg = "my test mail"

svr = smtplib.SMTP(mailserver)
# 设置为调试模式，就是在会话过程中会有输出信息
svr.set_debuglevel(1)
# ehlo命令，docmd方法包括了获取对方服务器返回信息，如果支持安全邮件，返回值里会有starttls提示
svr.docmd("EHLO server")
svr.starttls()  # <------ 这行就是新加的支持安全邮件的代码！
# auth login 命令
svr.docmd("AUTH LOGIN")
# 发送用户名，是base64编码过的，用send发送的，所以要用getreply获取返回信息
svr.send(base64.encodestring(username))
svr.getreply()
# 发送密码
svr.send(base64.encodestring(password))
svr.getreply()
# mail from, 发送邮件发送者
svr.docmd("MAIL FROM: <%s>" % from_addr)
# rcpt to, 邮件接收者
svr.docmd("RCPT TO: <%s>" % to_addr)
# data命令，开始发送数据
svr.docmd("DATA")
# 发送正文数据
svr.send(msg)
# 比如以 . 作为正文发送结束的标记
svr.send(" . ")
svr.getreply()
# 发送结束，退出
svr.quit()
