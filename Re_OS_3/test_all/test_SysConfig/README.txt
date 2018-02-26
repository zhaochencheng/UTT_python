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
                ------配置管理               test_32_003_Configuration_management(未实现)
                ------重启操作               test_32_004_Reboot_DUT(加入重启生效 判断)

        网络工具 test_Network_tools.py (未实现)

        系统日志

        计划任务 test_Task_plan.py (未实现)

