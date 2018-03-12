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



测试脚本