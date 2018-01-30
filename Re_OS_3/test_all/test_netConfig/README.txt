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
           ----wan口固定ip 配置与删除     test_1_001_wan_config_static  [使用显性等待,减少定位不到元素问题] [放自动截图]
           ----wan口DHCP  配置与释放      test_1_002_wan_config_DHCP  [使用显性等待,减少定位不到元素问题] [放自动截图]
           ----wan口PPPOE 配置与删除      test_1_003_wan_config_PPPoE (引言,判断网通)

    内网配置 test_Lan_config.py
           ----lan口默认配置              test_2_001_lanconfig (待实现)
           ----vlan配置与删除             test_2_002_vlan_lanconfig

    DHCP服务

    端口映射 test_Port_mapping.py
           ----静态映射配置,修改与删除    test_04_001_static_port_mapping[os对截图文件夹清空,再放截图][对配置的端口进行验证]
           ----NAT规则 配置与删除         test_04_002_nat_rule[对nat规则的判断]
           ----DMZ主机配置                test_04_003_DMZ [#添加DMZ 生效 方法 ][#单个wan口DMZ 配置]
    路由配置 test_router_config.py
           -----静态路由配置与删除        test_05_001_staticRouter[要考虑如何将所有接口都能绑定 进行测试]

    动态域名

    交换配置



测试脚本