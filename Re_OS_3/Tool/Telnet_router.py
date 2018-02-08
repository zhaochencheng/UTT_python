
# @Time    : 2018/2/8 13:30
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : Telnet_router.py
# @Software: PyCharm Community Edition
import telnetlib
class telnet_Router():
    def telnet_router(self,host,string):
        u'''telnet到路由器中'''
        name  = b"UTT login: "
        pwd = b"Password: "
        user = "admin"
        password = "admin"
        tn = telnetlib.Telnet(host,port=60023)
        tn.read_until(name)
        tn.write(user.encode("ascii")+b'\n')
        if password:
            tn.read_until(pwd)
            tn.write(password.encode('ascii')+b'\n')
        # tn.write(b"uname -s\n") #ReOS SE
        # tn.write(b"uname -n\n") #UTT
        # tn.write(b"uname -r\n") #2.6.35
        # tn.write(b"uname -v\n") #QV4240G v3.0.0-171106
        tn.write(b"%s\n"%string)
        # tn.write(b"uname -m\n")
        # tn.write(b'ls -l\n')
        tn.write(b"exit\n")
        print(tn.read_all().decode("ascii"))
        tn.close()

if __name__ == '__main__':
    telnet_Router().telnet_router("192.168.2.1",b"uname -v")

