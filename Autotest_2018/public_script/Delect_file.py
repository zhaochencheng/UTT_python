# -*- coding: utf-8 -*-
# @Time    : 2018/2/26 11:14
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : Delect_file.py
# @Software: PyCharm Community Edition
import os
class Del_file():
    '''清空某个目录'''
    def delect_file(self,path):
        ls = os.listdir(path)
        for i in ls:
            c_path = os.path.join(path, i)
            if os.path.isdir(c_path):
                Del_file().delect_file(c_path)
            else:
                os.remove(c_path)
if __name__ == '__main__':
    path = r"G:\github\UTT_python\Autotest_2018\screen_shoot"
    Del_file().delect_file(path)