# -*- coding: utf-8 -*-
# @Time    : 2018/2/7 21:10
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : run_all2.py
# @Software: PyCharm Community Edition
import unittest
import os
import HTMLTestRunnerXL
from Utt.test_DP.test_001_AP_offline import *
from Utt.test_DP.test_002_AP_reboot import *
from Utt.test_DP.test_003_AP_Poe import AP_Poe
from Utt.test_DP.test_006_switch import Switch
from Utt.test_DP.test_005_APconfig import APconfig
from Utt.tool.mail import *

import  HTMLTestRunner
try:
    # 用例路径
    # case_path = os.path.join(os.getcwd(), "test_MSG")
    case_path = os.path.join(os.getcwd(), "test_DP")
    # 报告存放路径
    report_path = os.path.join(os.getcwd(), "test_report")
    # html报告文件
    report_abspath = os.path.join(
        report_path, "result_config.html")

    # 遍历case_path目录下；批量执行test_用例
    # discover = unittest.defaultTestLoader.discover(case_path,
    #                                                 pattern="test*.py",
    #                                                 top_level_dir=None)
    # #单个执行用例
    suit = unittest.TestSuite()
    suit.addTest(APconfig("test_APconfig"))
    # time.sleep(1)
    # suit.addTest(AP_Poe("test_AP_poe"))
    fp = open(report_abspath, "wb")
    #html报告格式 一
    # runner = HTMLTestRunnerXL.HTMLTestRunner(stream=fp,
    #                                        title=u'自动化测试报告,测试结果如下：',
    #                                        description=u'用例执行情况：')
    #Html报告格式 二
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'自动化测试报告,测试结果如下：',
                                           description=u'用例执行情况：')
    # 调用add_case函数返回值
    # runner.run(discover)  #执行用例
    runner.run(suit)
    fp.close()

    #调用邮件发送，自动发送邮件
    # file = Search_testReport(report_path)
    # send_email(file)
except Exception as err:
    print(err)