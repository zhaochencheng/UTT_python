# -*- coding: utf-8 -*-
# @Time    : 2018/1/19 16:25
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : config.py
# @Software: PyCharm Community Edition
#登陆 url 用户名 密码
url ="http://192.168.2.1"
username = "admin"
pwd = "admin"
''' 外网配置'''
#外网配置 wan口ip 子网掩码 网关地址
wan_ip = ["192.168.30.115","192.168.30.117","192.168.30.118","192.168.30.119"]
wan_ip1 = ["192.168.3.116","192.168.3.117","192.168.3.118","192.168.3.119"]

netmask = "255.255.255.0"

GWaddr1 ="192.168.3.5"
GWaddr ="192.168.30.1"
DNSaddr = "114.114.114.114"

#PPPOE 账号和密码  --- 应该用字典 写   后续修改
pppoeuser = ['1','2','3','4']
pppoepwd =['1','2','3','4']
