#coding:utf-8
from HTMLTestRunner import HTMLTestRunner
import time
from Autotest_2018.script.用户管理.用户状态 import 用户_状态
from Autotest_2018.script.网络配置.内网配置 import LAN口配置
from Autotest_2018.script.网络配置.单线路上网 import *

if __name__ == '__main__':

    suite=unittest.TestSuite()

    suite.addTest(单线路_固定IP上网("test_上网配置"))
    suite.addTest(单线路_固定IP上网("test_Cli验证"))
    suite.addTest(单线路_固定IP上网("test_上网测试"))
    suite.addTest(LAN口配置("test_LAN口配置"))
    suite.addTest(LAN口配置("test_LAN口验证"))
    suite.addTest(LAN口配置("test_LAN_VLAN配置"))
    suite.addTest(LAN口配置("test_LAN_VLAN验证"))
    suite.addTest(用户_状态("test_用户状态查看"))
    suite.addTest(用户_状态("test_临时用户加入分组"))

    #suite.addTest(单线路_动态IP上网("test_上网配置"))
    #suite.addTest(单线路_动态IP上网("test_Cli验证"))
    #suite.addTest(单线路_动态IP上网("test_上网测试"))

    #suite.addTest(单线路_PPPoE拨号上网("test_上网配置"))
    #suite.addTest(单线路_PPPoE拨号上网("test_Cli验证"))
    #suite.addTest(单线路_PPPoE拨号上网("test_上网测试"))





    #
    #Report_title  报告标题
    #software_path 待测试软件绝对路径
    #
    Report_title = '自动化测试报告'
    software_path = 'E:\Autotest_2018\software\\nv518GV2v3.0.0-171117.bin'
    #

    #
    soft = software_path.split('\\')
    soft_name = soft[len(soft)-1]
    Notes = '测试软件：' + soft_name
    #

    Logfilename= mklog_file()
    fp=open(Logfilename,'wb')
    runner=HTMLTestRunner(stream=fp,title=Report_title,description=Notes)
    runner.run(suite)
    fp.close()



