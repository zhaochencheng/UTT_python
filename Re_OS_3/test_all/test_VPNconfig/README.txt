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
