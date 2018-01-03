# -*- coding: utf-8 -*-
import os,time
import sys
'''
ping 工具；
'''
def ping_ip(ip):
    # ip = 'www.baidu.com'
    start_Time = int(time.time())
    return1 = os.system('ping -n 2 -w 2 %s' % ip)
    #ping [-t] [-a] [-n count] [-l length] [-f] [-i ttl]
    # [-v tos] [-r count] [-s count] [[-j -Host list] | [-k Host-list]] [-w timeout] destination-list
    count_True, count_False = 0, 0
    if return1:
        print('ping %s is fail' % ip)
        # ip_False.write(ip+'\n')
        count_False += 1
    else:
        print('ping %s is ok' % ip)
        # ip_True.write(ip+'\n')
        count_True += 1
    end_Time = int(time.time())
    print("time(秒)：", end_Time - start_Time, "s")
    print("ping通的ip数：", count_True, "   ping不通的ip数：", count_False)
if __name__ == '__main__':
    ping_ip('192.168.22.1')