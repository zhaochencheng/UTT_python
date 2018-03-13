该目录下为 要执行的test文件
即:执行的自动化用例;
要求:每个用例 之间没有关联性或依赖性;
    每个.py文件都是可以单独运行且可产生结果的用例

具体每个文件夹中test_** 可执行什么功能  请看每个文件夹中的README.txt文件






下附:总目录:
!!!! 警告:非作者 禁止修改以下内容!!!

#目录下内容为：

备注1:
      没有子项的标题为 "未实现" 部分
      () 内容为 "未实现" 部分
      [] 内容为 "可改进" 部分 ,但现有代码不会影响正常使用

备注2:
      此ui自动化测试,侧重 页面功能是否生效.
      对于页面 所有可操作元素 未完全覆盖到;
*****************************************
-----------------------------------------
网络配置：test_netConfig  [放自动截图]
     外网配置 test_wan_config.py
           ----wan口固定ip 配置与删除     test_01_001_wan_config_static  [使用显性等待,减少定位不到元素问题] [放自动截图]
                                            --2018/02/28 已添加显性等待、自动截图
           ----wan口DHCP  配置与释放      test_01_002_wan_config_DHCP  [使用显性等待,减少定位不到元素问题] [放自动截图]
                                            --2018/02/28 已添加显性等待、自动截图
           ----wan口PPPOE 配置与删除      test_01_003_wan_config_PPPoE (引言,判断网通)

    内网配置 test_Lan_config.py
           ----lan口默认配置              test_02_001_lanconfig (待实现)
           ----vlan配置与删除
                    vlan配置                      test_02_002_vlan_Lan_configure
                    将页面配置的vlan lan输出       test_02_003_vlan_Lan_web_show
                    将配置的vlan lan 删除          test_02_004_vlan_Lan_dele_config

    DHCP服务
           -----DHCP服务
                     DHCP服务配置               test_03_001_DHCP_server_config
                     将DHCP页面信息输出         test_03_002_DHCP_server_show
                     DHCP功能生效判断           test_03_003_DHCP_server_validate(未实现)(思路：查看DHCP客户端列表；看是否有主机)
                     DHCP服务配置删除           test_03_004_DHCP_server_delete

    端口映射 test_Port_mapping.py
           ----静态映射
                    静态映射配置          test_04_001_static_port_mapping_config
                    静态映射配置-页面信息正确  test_04_002_static_port_mapping_show
                    对配置静态端口映射 进行验证  test_04_003_static_port_mapping_validate(未实现)
                    静态映射删除          test_04_004_static_port_mapping_delect

           ----NAT规则
                    NAT规则EasyIP 配置           test_04_006_nat_rule_config_EasyIP
                    EasyIP配置-页面信息正确      test_04_007_nat_rule_show_EasyIP
                    验证EasyIP功能生效           test_04_008_nat_rule_EasyIP_validate(未实现)
                    将配置的EasyIP 信息删除      test_04_009_nat_rule_del_EasyIP

                    NAT规则 One2One配置          test_04_011_nat_rule_config_One2One
                    One2One配置-页面信息正确     test_04_012_nat_rule_show_One2One
                    验证One2One配置功能生效      test_04_013_nat_rule_One2One_validate(未实现)
                    将One2One配置 信息删除       test_04_014_nat_rule_del_One2One


           ----DMZ主机配置               test_04_003_DMZ [#添加DMZ 生效 方法][#单个wan口DMZ 配置]

    路由配置 test_rouger_config.py
            ----静态路由配置与删除
                    静态路由——配置         test_05_001_staticRouter_config
                    静态路由 页面信息正确  test_05_002_staticRouter_show
                    静态路由功能生效-判断  test_05_003_statciRouter_validate
                    静态路由配置信息 删除  test_05_004_staticRouter_del

            ----策略路由 开启 、关闭与策略路由配置   test_05_006_strategyRouter(重构)


    动态域名 test_DDNS.py
           -----动态域名
                    配置DDNS-uttcare            test_06_001_DDNS_uttcare_config
                    DDNS-uttcare信息输出        test_06_002_DDNS_uttcare_show
                    DDNS-uttcare功能生效验证    test_06_003_DDNS_uttcare_validate
                    DDNS-uttcare信息删除        test_06_004_DDNS_uttcare_del



    交换配置



无线扩展：test_WirelessExtension

    网络名称

    设备管理

    射频模板

    负载均衡

    软件管理


用户管理
   组织用户  test_organize_member.py
            ------组织成员配置与操作             test_13_001_accStatu[如何与下面的功能关联在一起]

   用户状态 test_accStatu.py
            ------用户状态显示与操作             test_14_001_accStatu[将本机ip拉黑导致无法再进入web页面。拉黑别的ip如何测试]

    用户认证

    黑名单 test_BlackList.py
            ----黑名单配置                              test_16_001_blacklist_config
            ----黑名单页面信息显示                      test_16_002_blacklist_show
            ----黑名单功能验证                          test_16_003_blacklist_validate(未实现)
            ----黑名单配置删除                          test_16_004_blacklist_delete

行为管理  test_BehaviorManagement
    行为管理 test_BehaviorManage.py
            ------ 行为管理配置与删除      test_17_001_behaviorMange[加入禁ping判断][考虑其他行为管理如何禁止]

    域名过滤 test_Dns_dnsFilter.py
            ------ 域名过滤开启与关闭      test_18_001_dnsfilter

    白名单

    电子通告 test_LectronicsNotice.py
            ------ 电子通告开启与关闭       test_20_001_lectronicsNotice

流量管理 test_TrafficManagement
        -----应用优先     test_Application_priority.py
                应用管理--开启                test_21_001_Application_priority_open
                办公优先配置                  test_21_002_Application_priority_Office_priority_config
                办公优先配置页面内容输出       test_21_003_Application_priority_Office_priority_show
                办公优先配置 功能生效          test_21_004_Application_priority_Office_priority_validate (未实现)
                办公优先配置删除               test_21_005_Application_priority_Office_priority_delect

                娱乐优先配置                   test_21_007_Application_priority_Entertainment_priority_config
                娱乐优先配置页面内容输出       test_21_008_Application_priority_Entertainment_priority_show
                娱乐优先配置 功能生效          test_21_009_Application_priority_Entertainment_priority_validate(未实现)
                娱乐优先配置删除               test_21_010_Application_priority_Entertainment_priority_delect
                应用管理--关闭                 test_21_011_Application_priority_close

        -----流量管理

防火墙
    访问控制

    连接控制

    攻击防护



VPN配置
    IPSec test_IPsec.py
        -----IPsec配置--对方动态连接到本地                 test_26_001_IPsec_dynamically_connected_local_config
        -----IPsec配置信息输出--对方动态连接到本地         test_26_002_IPsec_dynamically_connected_local_show
        -----IPsec功能验证--对方动态连接到本地             test_26_003_IPsec_dynamically_connected_local_validate
        -----IPsec配置删除--对方动态连接到本地             test_26_004_IPsec_dynamically_connected_local_delete

        -----IPsec配置--动态连接到网关                     test_26_006_IPsec_dynamically_connected_gateway_config
        -----IPsec信息显示--动态连接到网关                  test_26_007_IPsec_dynamically_connected_gateway_show
        -----IPsec功能验证--动态连接到网关                  test_26_008_IPsec_dynamically_connected_gateway_validate
        -----IPsec配置删除--动态连接到网关                  test_26_009_IPsec_dynamically_connected_gateway_delete

    PPTP/L2TP
        -----PPTP服务器配置                               test_27_001_PPTP_server_config
        -----PPTP配置--做服务端                            test_27_002_PPTP_as_server_config
        -----PPTP信息显示--做服务端                        test_27_003_PPTP_as_server_show
        -----PPTP功能验证--做服务端                        test_27_004_PPTP_as_server_validate
        -----PPTP配置删除--做服务端                        test_27_005_PPTP_as_server_delete

        -----PPTP配置--做客户端                            test_27_007_PPTP_as_Client_config
        -----PPTP信息显示--做客户端                         test_27_008_PPTP_as_Client_show
        -----PPTP功能验证--做服务端                         test_27_009_PPTP_as_Client_validate
        -----PPTP配置删除--做客户端                         test_27_010_PPTP_as_Client_delete

        ----L2TP服务器配置                                  test_27_012_L2TP_server_config
        ----L2TP配置--做服务端                              test_27_013_L2TP_as_server_config
        ----L2TP信息显示--做服务端                           test_27_014_L2TP_as_server_show
        ----L2TP功能验证--做服务端                           test_27_015_L2TP_as_server_validate
        ----L2TP配置删除--做服务端                           test_27_016_L2TP_as_server_delete

        ----L2TP配置--做客户端                              test_27_018_L2TP_as_Client_config
        ----L2TP信息显示--做客户端                          test_27_019_L2TP_as_Client_show
        ----L2TP功能验证--做客户端                          test_27_020_L2TP_as_Client_validate
        ----L2TP配置删除--做客户端                           test_27_021_L2TP_as_Client_delete
系统对象
    时间计划

    地址组

系统配置
       网管策略 test_NetManageStrate.py
                ------系统管理员的配置
                           系统管理员的配置          test_30_001_System_administrator_config
                           系统管理员页面信息输出    test_30_002_System_administrator_show
                           系统管理员功能生效验证    test_30_003_System_administrator_validate[多种方法论证 管理员的读写权限]
                           系统管理员配置删除        test_30_004_System_administrator_delect

                ------内网访问控制                   test_30_006_Intranet_access_control(未实现)

                ------远程管理
                           远程管理-开启              test_30_008_Remote_management_open
                           远程管理功能生效判断        test_30_009_Remote_management_validate[如何获取wan口ip，从页面获取？还是后台读wan口ip]
                           远程管理-关闭              test_30_010_Remote_managment_close

                ------网管访问策略                   test_30_012_Net_management_access_strategy(未实现)

                ------语言配置               test_30_013_language_select

        时钟管理 test_Clock_management.py
                ------时钟管理的配置       test_31_001_Clock_management

        系统维护 test_System_maintenance.py
                ------系统升级              test_32_001_System_upgrade(加入软件升级生效 判断)
                ------应用特征库显示         test_32_002_Application_feature_library
                ------配置管理               test_ 32_003_Configuration_management(未实现)
                ------重启操作               test_32_004_Reboot_DUT(加入重启生效 判断)

        网络工具 test_Network_tools.py (未实现)

        系统日志

        计划任务 test_Task_plan.py (未实现)

