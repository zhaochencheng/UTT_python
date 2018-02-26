# -*- coding: utf-8 -*-
# @Time    : 2018/1/19 16:25
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : config.py
# @Software: PyCharm Community Edition
#登陆 url 用户名 密码
url ="http://192.168.2.1"
# url ="http://117.71.57.195:8888"
username = "admin"
pwd = "admin"

#*****************************************************************#
''' 外网配置'''
#外网配置 wan口ip 子网掩码 网关地址
wan_ip = ["192.168.30.115","192.168.30.117","192.168.30.118","192.168.30.119"]
wan_ip1 = ["192.168.30.116","192.168.3.117","192.168.3.118","192.168.3.119"]

netmask = "255.255.255.0"
GWaddr1 ="192.168.30.1"
GWaddr ="192.168.30.1"
DNSaddr = "114.114.114.114"

#PPPOE 账号和密码  --- 应该用字典 写   后续修改
pppoeuser = ['1','2','3','4']
pppoepwd =['1','2','3','4']


#*****************************************************************#
'''内网配置'''






#vlan 配置
vlan_lanipname = ["222","223","224"]
vlan_ip = ["192.168.222.1","192.168.223.1","192.168.224.1"]
vlan_id = ["222","223","224"]

#*****************************************************************#
'''DHCP服务'''

#*****************************************************************#
'''端口映射'''

#静态映射
new_rulename = ["AC12","AC23"]
inaddr = ["192.168.2.33","192.168.2.55"]
inport = ["80","88"]
outport = ["8081","8888"]

#NAT规则
NAT_rulename = ["192.123","1212"]
inaddr_begin = ["192.168.2.3","192.168.2.22"]
inaddr_end = ["192.168.2.5","192.168.2.25"]
outaddr = ["192.168.30.22","192.168.30.55"]


#DMZ主机

globalDMZHost = "192.168.2.22"


#*****************************************************************#
'''路由配置'''
#静态路由
router_static_name =["333",'444']  #规则名称
rou_static_destNet = ["192.168.3.22","192.168.4.23"] #目的网络
rou_static_netmask= ["255.255.255.0","255.255.255.0"] #子网掩码
rou_static_GWay =["192.168.2.112","192.168.3.4"] #网关地址
rou_static_priority = ["1","2"] #优先级


#策略路由
router_strategy_name = ["ap","ac"]
router_RouteLevel = ['1','2']



#*****************************************************************#
'''无线扩展'''
#网络名称
net_name = ['123','34']
ssid = ["1232",'345']

#*****************************************************************#
'''用户管理'''
#组织成员
newtree = ["分组1","内网","god"]# 分组名称






#*****************************************************************#
'''行为管理'''
#行为管理
behavior_rulename =['12','43','额外']#规则名称
servername = ["ping",'FTP','ICMP'] #应用服务


#域名过滤
DNS_filter_rulename = ["163","baidu"]
DNS_filter_hostname = ["www.163.com","www.sina.com","www.taobao.com"]#过滤 域名



#*****************************************************************#
'''VPN配置'''
#ipsec
tunnelName = ['AUTO_test']
remoteip = ["172.168.0.1"]
shareKey = ["123456789"]












#*****************************************************************#
'''系统配置'''
#网管策略
admin_username =["reader","root"] # reader 权限为 ‘读’     root 权限为 ‘读写’
admin_password = ["reader","root"]

#时钟管理
NtpServerip = ["202.108.6.95","24.56.178.140" ]#服务器1 IP地址

#系统升级
update_path= "C:\\Users\\utt\\Desktop\\QV4240Gv3.0.0-171106.bin"
