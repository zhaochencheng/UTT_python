# -*- coding: utf-8 -*-
# @Time    : 2018/1/5 13:26
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : test_004_AP_Telnet.py
# @Software: PyCharm Community Edition

import unittest
import telnetlib
import time

class AP_telnet(unittest.TestCase):
    '''telnet到ap中'''
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_AP_telnet(self):
        '''/etc下导入config文件'''

        HOST = "192.168.2.117"
        user = "admin"
        password = "admin_default"
        f = open("telnet_gaotong.txt", "w")
        b = 0
        a = 0
        for i in range(300):
            try:
                tn = telnetlib.Telnet(HOST, port=60023, timeout=120)
                tn.read_until(b"DPtech login: ")
                tn.write(user.encode('ascii') + b"\n")
                if password:
                    tn.read_until(b"Password: ")
                    tn.write(password.encode('ascii') + b"\n")
                print("----------------*********************---------------------\n")
                print("第%d次导入" % i)
                f.writelines("----------------*********************---------------------\n")
                f.writelines(time.ctime())
                f.writelines("\n")
                f.writelines("---------第%d次导入-------" % i + "\n")
                for l in range(4):
                    print("  -*-*-*-再循环导入第%d次-*-*-*-  " % l)
                    # f.writelines("  -*-*-*-再循环导入第")
                    # f.writelines(str(l))
                    # f.writelines("次-*-*-*-  \n")
                    tn.write(b"cd /etc\n")
                    time.sleep(1)
                    tn.write(b"tftp -gr 1.txt  192.168.2.190 69\n")
                    time.sleep(15)
                    # tn.write(b"tftp -gr wifidog  192.168.2.190 69\n")
                    # time.sleep(4)
                    # tn.write(b"tftp -gr network  192.168.2.190 69\n")
                    tn.write(b"ls -l|grep txt\n")
                    time.sleep(2)
                    tn.write(b"\n")
                tn.write(b"exit\n")
                fal = tn.read_all().decode("ascii")
                f.writelines(fal)
                print(fal)
                tn.close()
                a += 1
                print("telnet success：", a)
                f.writelines("telnet  success：")
                f.writelines(str(a))
                f.writelines("\n")


            except Exception as E:
                try:
                    print(E)
                    b += 1
                    print("telnet  not success：", b)
                    print("第%d次导入" % i)
                    f.writelines("----------------*********************---------------------\n")
                    f.writelines(time.ctime())
                    f.writelines("\n")
                    f.writelines("第%d次导入" % i + "\n")
                    f.writelines("telnet  not success：")
                    f.writelines(str(b))
                    f.writelines("\n")

                    # f.writelines("导入失败原因为：",E+ "\n")
                except Exception as e:
                    print(e)

        f.close()


if __name__ == '__main__':
    unittest.main()

