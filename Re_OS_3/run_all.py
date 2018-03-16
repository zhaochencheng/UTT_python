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
from Re_OS_3.Public.Delect_file import Del_file
from Re_OS_3.test_all.test_BehaviorManagement.test_BehaviorManage import BehaviorManage
from Re_OS_3.test_all.test_BehaviorManagement.test_Dns_dnsFilter import DNS_filter
from Re_OS_3.test_all.test_BehaviorManagement.test_LectronicsNotice import lectronicsNotice
from Re_OS_3.test_all.test_SysConfig.test_Clock_management import Clock_management
from Re_OS_3.test_all.test_SysConfig.test_NetManageStrate import NetManageStrate
from Re_OS_3.test_all.test_SysConfig.test_System_maintenance import System_maintenance
from Re_OS_3.test_all.test_TrafficManagement.test_Application_priority import Application_priority
from Re_OS_3.test_all.test_UserManage.test_BlackList import Black_List
from Re_OS_3.test_all.test_UserManage.test_organize_member import Organization_member
from Re_OS_3.test_all.test_VPNconfig.test_IPsec import IPSec
from Re_OS_3.test_all.test_VPNconfig.test_L2TP import L2TP
from Re_OS_3.test_all.test_VPNconfig.test_PPTP import PPTP
from Re_OS_3.test_all.test_netConfig.test_DDNS import DDNS_config
from Re_OS_3.test_all.test_netConfig.test_DHCP_server import DHCP_config
from Re_OS_3.test_all.test_netConfig.test_Lan_config import Lan_config
from Re_OS_3.test_all.test_netConfig.test_wan_config import Wan_config
from Re_OS_3.test_all.test_netConfig.test_Port_mapping import Port_mapping
from Re_OS_3.test_all.test_netConfig.test_router_config import Router_config
from Re_OS_3.test_all.test_UserManage.test_accStatu import AccStatu

#对Screenshot 文件夹进行清空
cwd = os.getcwd()
print(cwd)
ScreenShot = cwd + "\Screenshot"
print(ScreenShot)
Del_file().delect_file(ScreenShot)
# 当前脚本所在文件真实路径
cur_path = os.path.dirname(os.path.realpath(__file__))
#用例路径
case_path = os.path.join(cur_path,"test_all")
#报告存放路径
report_path = os.path.join(cur_path,"Report")
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
'''wan口配置'''
suit.addTest(Wan_config("test_01_001_wan_static_config"))
suit.addTest(Wan_config("test_01_002_wan_static_show"))
suit.addTest(Wan_config("test_01_003_wan_static_webcheck"))
suit.addTest(Wan_config("test_01_004_wan_static_validate"))
suit.addTest(Wan_config("test_01_005_wan_static_config_delete"))
suit.addTest(Wan_config("test_01_007_wan_DHCP_config"))
suit.addTest(Wan_config("test_01_008_wan_DHCP_show"))
suit.addTest(Wan_config("test_01_009_wan_DHCP_webcheck"))
suit.addTest(Wan_config("test_01_010_wan_DHCP_validate"))
suit.addTest(Wan_config("test_01_011_wan_DHCP_delete"))
suit.addTest(Wan_config("test_01_013_wan_PPPoE_config"))
suit.addTest(Wan_config("test_01_014_wan_PPPoE_show"))


'''内网配置'''
suit.addTest(Lan_config("test_02_002_vlan_Lan_configure"))
suit.addTest(Lan_config("test_02_003_vlan_Lan_web_show"))
suit.addTest(Lan_config("test_02_004_vlan_Lan_dele_config"))
'''#DHCP配置'''
suit.addTest(DHCP_config("test_03_001_DHCP_server_config"))
suit.addTest(DHCP_config("test_03_002_DHCP_server_show"))
suit.addTest(DHCP_config("test_03_003_DHCP_server_validate"))
suit.addTest(DHCP_config("test_03_004_DHCP_server_delete"))
'''#端口映射'''
suit.addTest(Port_mapping("test_04_001_static_port_mapping_config"))
suit.addTest(Port_mapping("test_04_002_static_port_mapping_show"))
suit.addTest(Port_mapping("test_04_003_static_port_mapping_validate"))
suit.addTest(Port_mapping("test_04_004_static_port_mapping_delect"))
suit.addTest(Port_mapping("test_04_006_nat_rule_config_EasyIP"))
suit.addTest(Port_mapping("test_04_007_nat_rule_show_EasyIP"))
suit.addTest(Port_mapping("test_04_008_nat_rule_EasyIP_validate"))
suit.addTest(Port_mapping("test_04_009_nat_rule_del_EasyIP"))
suit.addTest(Port_mapping("test_04_011_nat_rule_config_One2One"))
suit.addTest(Port_mapping("test_04_012_nat_rule_show_One2One"))
suit.addTest(Port_mapping("test_04_013_nat_rule_One2One_validate"))
suit.addTest(Port_mapping("test_04_014_nat_rule_del_One2One"))
suit.addTest(Port_mapping("test_04_016_DMZ"))
'''#路由配置'''
suit.addTest(Router_config("test_05_001_staticRouter_config"))
suit.addTest(Router_config("test_05_002_staticRouter_show"))
suit.addTest(Router_config("test_05_003_statciRouter_validate"))
suit.addTest(Router_config("test_05_004_staticRouter_del"))
suit.addTest(Router_config("test_05_006_strategyRouter"))
'''#动态域名'''
suit.addTest(DDNS_config("test_06_001_DDNS_uttcare_config"))
suit.addTest(DDNS_config("test_06_002_DDNS_uttcare_show"))
suit.addTest(DDNS_config("test_06_003_DDNS_uttcare_validate"))
suit.addTest(DDNS_config("test_06_004_DDNS_uttcare_del"))
'''组织成员'''
suit.addTest(Organization_member("test_13_001_Organization_member_config"))
suit.addTest(Organization_member("test_13_002_Organization_member_show"))
'''用户状态'''
suit.addTest(AccStatu("test_14_001_accStatu_Users_joingroups"))
suit.addTest(AccStatu("test_14_002_accStatu_Users_show"))
suit.addTest(AccStatu("test_14_003_accStatu_User_into_blacklist"))
'''黑名单'''
suit.addTest(Black_List("test_16_001_blacklist_config"))
suit.addTest(Black_List("test_16_002_blacklist_show"))
suit.addTest(Black_List("test_16_003_blacklist_validate"))
suit.addTest(Black_List("test_16_004_blacklist_delete"))
'''行为管理'''
suit.addTest(BehaviorManage("test_17_001_behaviorMange_config"))
suit.addTest(BehaviorManage("test_17_002_behaviorMange_show"))
suit.addTest(BehaviorManage("test_17_003_behaviorMange_validate"))
suit.addTest(BehaviorManage("test_17_004_behaviorMange_delete"))
'''域名过滤'''
suit.addTest(DNS_filter("test_18_001_dnsfilter_open"))
suit.addTest(DNS_filter("test_18_002_dnsfilter_config"))
suit.addTest(DNS_filter("test_18_003_dnsfilter_show"))
suit.addTest(DNS_filter("test_18_004_dnsfilter_validate"))
suit.addTest(DNS_filter("test_18_005_dnsfilter_close"))
suit.addTest(DNS_filter("test_18_006_dnsfilter_close_check"))
'''电子通告'''
suit.addTest(lectronicsNotice("test_20_001_lectronicsNotic_config"))
suit.addTest(lectronicsNotice("test_20_002_lectronicsNotic_validate"))
suit.addTest(lectronicsNotice("test_20_003_lectronicsNotic_close"))
'''应用优先'''
suit.addTest(Application_priority("test_21_001_Application_priority_open"))
suit.addTest(Application_priority("test_21_002_Application_priority_Office_priority_config"))
suit.addTest(Application_priority("test_21_003_Application_priority_Office_priority_show"))
suit.addTest(Application_priority("test_21_004_Application_priority_Office_priority_validate"))
suit.addTest(Application_priority("test_21_005_Application_priority_Office_priority_delect"))
suit.addTest(Application_priority("test_21_007_Application_priority_Entertainment_priority_config"))
suit.addTest(Application_priority("test_21_008_Application_priority_Entertainment_priority_show"))
suit.addTest(Application_priority("test_21_009_Application_priority_Entertainment_priority_validate"))
suit.addTest(Application_priority("test_21_010_Application_priority_Entertainment_priority_delect"))
suit.addTest(Application_priority("test_21_011_Application_priority_close"))
'''IPsec'''
suit.addTest(IPSec("test_26_001_IPsec_dynamically_connected_local_config"))
suit.addTest(IPSec("test_26_002_IPsec_dynamically_connected_local_show"))
suit.addTest(IPSec("test_26_003_IPsec_dynamically_connected_local_validate"))
suit.addTest(IPSec("test_26_004_IPsec_dynamically_connected_local_delete"))
suit.addTest(IPSec("test_26_006_IPsec_dynamically_connected_gateway_config"))
suit.addTest(IPSec("test_26_007_IPsec_dynamically_connected_gateway_show"))
suit.addTest(IPSec("test_26_008_IPsec_dynamically_connected_gateway_validate"))
suit.addTest(IPSec("test_26_009_IPsec_dynamically_connected_gateway_delete"))
'''PPTP/L2TP'''
suit.addTest(PPTP("test_27_001_PPTP_server_config"))
suit.addTest(PPTP("test_27_002_PPTP_as_server_config"))
suit.addTest(PPTP("test_27_003_PPTP_as_server_show"))
suit.addTest(PPTP("test_27_004_PPTP_as_server_validate"))
suit.addTest(PPTP("test_27_005_PPTP_as_server_delete"))
suit.addTest(PPTP("test_27_007_PPTP_as_Client_config"))
suit.addTest(PPTP("test_27_008_PPTP_as_Client_show"))
suit.addTest(PPTP("test_27_009_PPTP_as_Client_validate"))
suit.addTest(PPTP("test_27_010_PPTP_as_Client_delete"))
suit.addTest(L2TP("test_27_012_L2TP_server_config"))
suit.addTest(L2TP("test_27_013_L2TP_as_server_config"))
suit.addTest(L2TP("test_27_014_L2TP_as_server_show"))
suit.addTest(L2TP("test_27_015_L2TP_as_server_validate"))
suit.addTest(L2TP("test_27_016_L2TP_as_server_delete"))
suit.addTest(L2TP("test_27_018_L2TP_as_Client_config"))
suit.addTest(L2TP("test_27_019_L2TP_as_Client_show"))
suit.addTest(L2TP("test_27_020_L2TP_as_Client_validate"))
suit.addTest(L2TP("test_27_021_L2TP_as_Client_delete"))
'''网关策略'''
suit.addTest(NetManageStrate("test_30_001_System_administrator_config"))
suit.addTest(NetManageStrate("test_30_002_System_administrator_show"))
suit.addTest(NetManageStrate("test_30_003_System_administrator_validate"))
suit.addTest(NetManageStrate("test_30_004_System_administrator_delect"))
suit.addTest(NetManageStrate("test_30_006_Intranet_access_control"))
suit.addTest(NetManageStrate("test_30_008_Remote_management_open"))
suit.addTest(NetManageStrate("test_30_009_Remote_management_validate"))
suit.addTest(NetManageStrate("test_30_010_Remote_managment_close"))
suit.addTest(NetManageStrate("test_30_012_Net_management_access_strategy"))
suit.addTest(NetManageStrate("test_30_013_language_select"))
'''时钟管理'''
suit.addTest(Clock_management("test_31_001_Clock_management"))
'''系统维护'''
suit.addTest(System_maintenance("test_32_001_System_upgrade"))
suit.addTest(System_maintenance("test_32_002_Application_feature_library"))
suit.addTest(System_maintenance("test_32_003_Configuration_management"))
suit.addTest(System_maintenance("test_32_004_Reboot_DUT"))


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

