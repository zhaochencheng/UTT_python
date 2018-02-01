# -*- coding: utf-8 -*-
# @Time    : 2018/1/30 11:28
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : Ping.py
# @Software: PyCharm Community Edition
import os,time
import sys
'''
ping 工具；
'''
class Ping():
    def ping_IP(self,ip):
        a = os.system('ping -n 2 -w 2 %s'% ip)
        # print(type(a))
        # print(a)
        #ping 通 a = 0  ;ping 不通a = 1
        if a == True:
            print('ping %s is fail' % ip)
            #如果ping 不通 会抛出异常
            raise BaseException("ping 不通该%s 地址 "%ip)
        else:
            # print(a)
            print('ping %s is ok' % ip)
            return False
if __name__ == '__main__':
    ip = ["192.168.30.1","192.168.30.2"]
    # ping = Ping().ping_IP(ip)
    # for i in range(len(ip)):
        # ping = Ping().ping_IP(ip[i])
    try:
        ping = Ping().ping_IP("www.baidu.com")
    except BaseException as E:
        # print("ping 不通配置中的ip")
        print("error",E)
        print(type(E))
        if E :
            print("功能生效")
        else:
            raise BaseException("功能生效不生效；未禁ping")

    # ping.ping_IP(ip)