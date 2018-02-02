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
           ----wan口DHCP  配置与释放      test_01_002_wan_config_DHCP  [使用显性等待,减少定位不到元素问题] [放自动截图]
           ----wan口PPPOE 配置与删除      test_01_003_wan_config_PPPoE (引言,判断网通)

    内网配置 test_Lan_config.py
           ----lan口默认配置              test_02_001_lanconfig (待实现)
           ----vlan配置与删除             test_02_002_vlan_lanconfig

    DHCP服务

    端口映射 test_Port_mapping.py [未加判断该功能是否生效]
           ----静态映射配置,修改与删除    test_04_001_static_port_mapping[os对截图文件夹清空,再放截图][对配置的端口进行验证]
           ----NAT规则 配置与删除        test_04_002_nat_rule
           ----DMZ主机配置               test_04_003_DMZ [#添加DMZ 生效 方法][#单个wan口DMZ 配置]
    路由配置 test_rouger_config.py
            ----静态路由配置与删除        test_05_001_staticRouter
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

行为管理  test_BehaviorManagement
    行为管理 test_BehaviorManage.py
            ------ 行为管理配置与删除      test_17_001_behaviorMange[加入禁ping判断][考虑其他行为管理如何禁止]

    域名过滤 test_Dns_dnsFilter.py
            ------ 域名过滤开启与关闭      test_18_001_dnsfilter

    白名单

    电子通告


流量管理

防火墙

VPN配置

系统对象

系统配置

