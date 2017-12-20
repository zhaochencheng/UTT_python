# coding:utf-8
import unittest
import os
# import HTMLTestRunnerXL
from Utt.tool.mail import *

import  HTMLTestRunner
try:
    # 用例路径
    case_path = os.path.join(os.getcwd(), "test_MSG")
    # 报告存放路径
    report_path = os.path.join(os.getcwd(), "test_report")
    # html报告文件
    report_abspath = os.path.join(
        report_path, "result.html")

    discover = unittest.defaultTestLoader.discover(case_path,
                                                    pattern="test*.py",
                                                    top_level_dir=None)

    fp = open(report_abspath, "wb")

    # runner = HTMLTestRunnerXL.HTMLTestRunner(stream=fp,
    #                                        title=u'自动化测试报告,测试结果如下：',
    #                                        description=u'用例执行情况：')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'自动化测试报告,测试结果如下：',
                                           description=u'用例执行情况：')

    # 调用add_case函数返回值
    runner.run(discover)
    fp.close()

    #调用邮件发送，自动发送邮件
    file = Search_testReport(report_path)
    send_email(file)
except Exception as err:
    print(err)