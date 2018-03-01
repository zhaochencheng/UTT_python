# -*- coding: utf-8 -*-
# @Time    : 2018/3/1 17:24
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : study_os.py
# @Software: PyCharm Community Edition
import os
print(__file__)
#获取当前脚本的真实路径
cur_path = os.path.realpath(__file__)
print("获取当前脚本的真实路径:",cur_path)
#获取脚本的名称
name = os.path.basename(cur_path)
print("获取脚本的名称:",name)
#获取当前脚本的文件夹
file_path = os.path.dirname(cur_path)
print("获取当前脚本的文件夹:",file_path)
#获取上一级文件夹
par_path = os.path.dirname(file_path)
print("获取上一级文件夹:",par_path)
#拼接文件路径
ta_path = os.path.join(par_path,"test001")
print("拼接文件路径",ta_path)
#获取其他文件夹
ta_path1 = os.path.join(par_path,"ke10")
print(ta_path1)
#判断文件夹是否存在
t = os.path.exists(ta_path)
print(t)
if not t:
    os.mkdir(ta_path)
    print(ta_path)
'''

常用方法：

1. os.name——判断现在正在实用的平台，Windows 返回 ‘nt'; Linux 返回’posix'

2. os.getcwd()——得到当前工作的目录。

3. os.listdir()——指定所有目录下所有的文件和目录名。

4. os.remove()——删除指定文件

5. os.rmdir()——删除指定目录

6. os.mkdir()——创建目录

　　注意：这样只能建立一层，要想递归建立可用：os.makedirs()

7. os.path.isfile()——判断指定对象是否为文件。是返回True,否则False

8. os.path.isdir()——判断指定对象是否为目录。是True,否则False。

9. os.path.exists()——检验指定的对象是否存在。是True,否则False.

10. os.path.split()——返回路径的目录和文件名。

11. os.getcwd()——获得当前工作的目录（get current work dir)

12. os.system()——执行shell命令。

13. os.chdir()——改变目录到指定目录

14. os.path.getsize()——获得文件的大小，如果为目录，返回0

15. os.path.abspath()——获得绝对路径。

16. os.path.join(path, name)——连接目录和文件名。

17.os.path.basename(path)——返回文件名

18. os.path.dirname(path)——返回文件路径
'''
path = os.path.abspath(cur_path)
print("获得绝对路径:",path)
print("返回路径的目录和文件名:",os.path.split(path))