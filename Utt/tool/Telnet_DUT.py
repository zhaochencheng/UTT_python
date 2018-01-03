# -*- coding: utf-8 -*-
# @Time    : 2017/12/28 11:26
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : Telnet_DUT.py
# @Software: PyCharm Community Edition
import telnetlib

def telnet_dut(string):
    HOST = "192.168.1.1"
    name = b"<DPTECH>"
    user = "admin"
    password = "admin"

    tn = telnetlib.Telnet(HOST, port=23)
    tn.read_until(name)
    # tn.write(user.encode('ascii') + b"\n")
    # if password:
    #     tn.read_until(b"Password: ")
    #     tn.write(password.encode('ascii') + b"\n")
    # tn.write(b"%s"%(string))
    tn.write(b"telnet 192.168.2.105 60023\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii'))
    tn.close()
if __name__ == '__main__':
    string = b"ps\n"
    telnet_dut(string)