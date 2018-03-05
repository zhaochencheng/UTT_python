# -*- coding: utf-8 -*-
# @Time    : 2018/3/5 9:56
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : game.py
# @Software: PyCharm Community Edition
import random
def caishuzi():
    print("请给出一个区间范围")
    while 1:
        a = input("最小值：")
        b = input("最大值：")
        if a == '' or b =='' :
            print("区间值 不能为空！")
        else:
            if int(a)>int(b):
                a,b=b,a
            print("区间为:[%s-%s]"%(a,b))
            break
    c = random.randint(int(a),int(b))
    print("标准值",c,"方便自己猜数！！！")
    while 1:
        d = input("请输入猜测数字：")
        if d == '':
            print("输入值不能为空!")
        else:
            if int(d) < c:
                print("当前数字 %s 小于 标准值"%d)
            elif int(d)>c:
                print("当前数字 %s 大于 标准值"%d)
            elif int(d) == c:
                print("**恭喜你，你猜对了！**")
                break
if __name__ == '__main__':
    caishuzi()