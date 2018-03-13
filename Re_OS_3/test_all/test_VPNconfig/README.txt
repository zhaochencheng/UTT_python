#!!!! 警告:非作者 禁止修改以下内容!!!

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