# coding: utf-8

import json
import hashlib
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from .admin_manger import AdminManger


class EmailManger(object):

    def __init__(self):
        self.smtp_server = 'smtp.163.com'

    # _format_addr()来格式化一个邮件地址
    def _format_addr(self, s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    def send_email_from_to(self, from_addr, from_passwd, to_addr, msg):

        msg = MIMEText(msg, 'plain', 'utf-8')
        msg['From'] = self._format_addr('管理者 <%s>' % from_addr)
        # msg['To']接收的是字符串而不是list，如果有多个邮件地址，用,分隔即可
        msg['To'] = self._format_addr('{}'.format(to_addr))
        msg['Subject'] = Header('来自wiki的反馈', 'utf-8').encode()

        # SMTP协议默认端口是25
        server = smtplib.SMTP(self.smtp_server, 25)
        # set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息
        server.set_debuglevel(1)
        server.login(from_addr, from_passwd)
        # sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list
        # as_string()把MIMEText对象变成str
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()


    def send_email(self, email_data, to_addr):
        msg = email_data
        admin = AdminManger()
        admin_data = admin.get_email()
        if admin_data:

            from_addr = admin_data.get('email', '')
            password = admin_data.get('email_password', '')
            self.send_email_from_to(from_addr, password, to_addr, msg)


