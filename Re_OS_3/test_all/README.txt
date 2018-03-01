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
网络配置：test_netConfig
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

    端口映射 test_Port_mapping.py [未加判断该功能是否生效]
           ----静态映射配置,修改与删除
                     静态映射配置                     test_04_001_static_port_mapping_config
                     静态映射配置-页面信息正确              test_04_002_static_port_mapping_show[加出错自动截图]
                     对配置静态端口映射 进行验证       test_04_003_static_port_mapping_validate (未实现)
                     静态映射删除                     test_04_004_static_port_mapping_delect

           ----NAT规则 配置与删除
                     NAT规则EasyIP 配置                 test_04_006_nat_rule_config_EasyIP
                     EasyIP配置-页面信息正确             test_04_007_nat_rule_show_EasyIP[加出错自动截图]
                     验证EasyIP功能生效                  test_04_008_nat_rule_EasyIP_validate (未实现)
                     将配置的EasyIP 信息删除             test_04_009_nat_rule_del_EasyIP

                     NAT规则 One2One配置                  test_04_011_nat_rule_config_One2One
                     One2One配置-页面信息正确             test_04_012_nat_rule_show_One2One
                     验证One2One功能生效                  test_04_013_nat_rule_One2One_validate (未实现)
                     将配置的One2One 信息删除             test_04_014_nat_rule_del_One2One

           ----DMZ主机配置               test_04_003_DMZ [#添加DMZ 生效 方法][#单个wan口DMZ 配置]





    路由配置 test_rouger_config.py
            ----静态路由配置与删除
                    静态路由——配置        test_05_001_staticRouter_config
                    静态路由 页面信息正确  test_05_002_staticRouter_show
                    静态路由功能生效-判断  test_05_003_statciRouter_validate[考虑ping怎么验证最为恰当]
                    静态路由配置信息 删除  test_05_004_staticRouter_del

            ----策略路由 开启 、关闭与策略路由配置   test_05_002_strategyRouter（未实现）


    动态域名 test_DDNS.py
           -----动态域名的新增与删除   test_006_ddns[已加入判断 ddns功能是否生效][-----如果打不开怎么办]

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

    黑名单

行为管理  test_BehaviorManagement
    行为管理 test_BehaviorManage.py
            ------ 行为管理配置与删除      test_17_001_behaviorMange[加入禁ping判断][考虑其他行为管理如何禁止]

    域名过滤 test_Dns_dnsFilter.py
            ------ 域名过滤开启与关闭      test_18_001_dnsfilter

    白名单

    电子通告 test_LectronicsNotice.py
            ------ 电子通告开启与关闭       test_20_001_lectronicsNotice

流量管理 test_TrafficManagement
       应用优先   test_Application_priority.py
            -----应用管理开启-操作-关闭        test_21_001_Application_priority
       流量管理
            -----


防火墙
    访问控制

    连接控制

    攻击防护


VPN配置
    IPSec

    PPTP/L2TP

系统对象
    时间计划

    地址组

系统配置
        网管策略 test_NetManageStrate.py
                ------系统管理员的配置    test_30_001_System_administrator[多种方法论证 管理员的读写权限]
                ------内网访问控制        test_30_002_Intranet_access_control(未实现)
                ------远程管理            test_30_003_Remote_management[如何获取wan口ip，从页面获取？还是后台读wan口ip]
                ------网管访问策略         test_30_004_Net_management_access_strategy(未实现)
                ------语言配置            test_30_005_language_select

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

