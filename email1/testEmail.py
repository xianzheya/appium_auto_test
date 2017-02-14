# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

pas = "cukpvvzmamcwbfdh"
sender = '836333664@qq.com'
receivers = ['836333664@qq.com','zhe.xiao@qunar.com']

message = MIMEText("PTTHON EMAIL TEST ...", 'plain', 'UTF-8')
#发件人
message['from'] = Header("菜鸟test","utf-8")
#收件人
message['to'] = Header("菜鸟", "utf-8")
#主题
subject = "python 邮箱测试"
message["Subject"] = Header(subject, "utf-8")

try:
    #smtpObj = smtplib.SMTP('smtp.qq.com',port=587)
    smtpObj = smtplib.SMTP()
    #smtpObj.set_debuglevel(1)
    #使用starttls加密
    smtpObj.connect(host='smtp.qq.com', port=587, source_address=None)
    smtpObj.starttls()
    #登录邮箱
    smtpObj.login("836333664@qq.com",pas)
    smtpObj.sendmail(sender, receivers,message.as_string())
    print("邮件发送成功")
    smtpObj.quit()
except smtplib.SMTPException as e:
    #smtpObj.quit()
    print(e)
    print("Error: 无法发送邮件")
    smtpObj.quit()