# -*- coding: utf-8 -*-
# @Time    : 2018/1/21 13:45
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : run_all.py
# @Software: PyCharm Community Edition
import HTMLTestRunner
import os
import unittest
from Re_OS_3.Tool.mail import *
from Re_OS_3.test_all.test_netConfig.test_wan_config import Wan_config

#用例路径
case_path = os.path.join(os.getcwd(),"test_all")
#报告存放路径
report_path = os.path.join(os.getcwd(),"Report")
#html报告文件
report_abspath = os.path.join(report_path,"result.html")

'''方法 一 '''
# 遍历case_path目录下；批量执行test_用例
# discover = unittest.defaultTestLoader.discover(case_path,
#                                                 pattern="test*.py",
#                                                 top_level_dir=None)
'''方法 二'''
#手动添加单个用例
suit = unittest.TestSuite()
suit.addTest(Wan_config("test_1_001_wan_config_static"))
suit.addTest(Wan_config("test_1_002_wan_config_DHCP"))
suit.addTest(Wan_config("test_1_003_wan_config_PPPoE"))


fp = open(report_abspath,"wb")
#Html报告格式
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'自动化测试报告,测试结果如下：',
                                           description=u'用例执行情况：')
runner.run(suit)
fp.close()
# 调用邮件发送，自动发送邮件
# file = Search_testReport(report_path)
# send_email(file)

