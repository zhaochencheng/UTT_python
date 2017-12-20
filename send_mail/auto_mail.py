# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 14:14
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : auto_mail.py
# @Software: PyCharm Community Edition
import smtplib
import email.mime.multipart
import email.mime.text
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def send_mail():
    msg = email.mime.multipart.MIMEMultipart()
    msgFrom = '18856361920@163.com' #从该邮箱发送
    # msgTo = 'zhao.chencheng@utt.com.cn' #发送到该邮箱
    msgTo = '907779487@qq.com'  # 发送到该邮箱
    smtpSever='smtp.163.com' # 163邮箱的smtp Sever地址
    smtpPort = '25' #开放的端口
    sqm='utt31801'  # 在登录smtp时需要login中的密码应当使用授权码而非账户密码

    msg['from'] = msgFrom
    msg['to'] = msgTo
    msg['subject'] = 'Python自动邮件test-'
    content = '''
    你好:
        这是一封python3发送的邮件
    '''
    txt = email.mime.text.MIMEText(content)
    msg.attach(txt)
    #构造附件1，传送当前目录下的test.txt文件
    sendfile = open('result.html',"rb").read()
    att = MIMEText(sendfile,'html','utf-8')
    att['Content-Type'] ='applocation/octet-stream'
    # 这里的filename可以任意写，写什么名字 邮件中就显示什么名字
    att['Content-Dispostion']='attachment;filename:result.html'
    msg.attach(att)

    smtp = smtplib.SMTP()
    #smtplib的connect（连接到邮件服务器）、login（登陆验证）、sendmail（发送邮件）
    smtp.connect(smtpSever, smtpPort)
    smtp.login(msgFrom, sqm)
    smtp.sendmail(msgFrom, msgTo, msg.as_string())
    # s = smtplib.SMTP("localhost")
    # s.send_message(msg)
    smtp.quit()
if __name__ == '__main__':
    send_mail()