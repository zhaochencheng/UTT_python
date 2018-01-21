# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 15:34
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : mail.py
# @Software: PyCharm Community Edition
import smtplib
import email.mime.multipart
import email.mime.text
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os, datetime, time


def Search_testReport(result_dir):
    '''查找该目录下 最新的文件'''
    # result_dir = 'F:\\untitled\\send_mail'
    lists = os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir + "\\" + fn) if not
    os.path.isdir(result_dir + "\\" + fn) else 0)
    print('最新的文件为： ' + lists[-1])
    file = os.path.join(result_dir, lists[-1])
    print(file)
    return  file


def send_email(file):
    msg = email.mime.multipart.MIMEMultipart()
    sendAddr='18856361920@163.com' #发件人
    password='utt31801' # 在登录smtp时需要login中的密码应当使用授权码而非账户密码
    # 单个收件人
    recipientAddrs=['zhao.chencheng@utt.com.cn']
    # #多个收件人
    # recipientAddrs = ['zhao.chencheng@utt.com.cn',"907779487@qq.com"]

    smtpHost = 'smtp.163.com'  # 163邮箱的smtp Sever地址
    smtpPort = '25'  # 开放的端口

    subject = '自动化测试报告'  #邮件主题
    content = '这是一封来自 Python 编写的测试邮件。' #邮件正文
    msg['from'] = sendAddr
    msg['to'] = ";".join(recipientAddrs)
    msg['subject'] = subject

    txt = email.mime.text.MIMEText(content, 'plain', 'utf-8')
    msg.attach(txt)

    # 添加附件，
    part = MIMEApplication(open(file,'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename=file)
    msg.attach(part)

    smtp = smtplib.SMTP()
    smtp.connect(smtpHost, smtpPort)
    smtp.login(sendAddr, password)
    smtp.sendmail(sendAddr, recipientAddrs, str(msg))
    print("邮件发送成功！")
    smtp.quit()
# if __name__ == '__main__':
#     try:
#         result_dir = 'F:\\untitled\\send_mail'
#         file = Search_testReport(result_dir)
#         send_email(file)
#     except Exception as err:
#         print(err)