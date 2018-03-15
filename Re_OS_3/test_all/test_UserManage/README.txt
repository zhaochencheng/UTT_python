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

用户管理
    组织用户 test_organize_member.py
            ------组织成员配置                test_13_001_Organization_member_config
            ------组织成员页面信息输出         test_13_002_Organization_member_show

    用户状态 test_accStatu.py
            ------将临时用户加入分组中            test_14_001_accStatu_Users_joingroups
            ------将用户信息输出                  test_14_002_accStatu_Users_show
            -------将某个用户拉黑                 test_14_003_accStatu_User_into_blacklist

    用户认证

    黑名单 test_BlackList.py
        ----黑名单配置           test_16_001_blacklist_config
        ----黑名单页面信息显示       test_16_002_blacklist_show
        ----黑名单功能验证         test_16_003_blacklist_validate(未实现)
        ----黑名单配置删除         test_16_004_blacklist_delete
