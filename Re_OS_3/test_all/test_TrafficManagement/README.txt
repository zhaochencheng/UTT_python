
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
流量管理 test_TrafficManagement
        -----应用优先    test_Application_priority.py
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