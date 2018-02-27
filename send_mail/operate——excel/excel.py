# -*- coding: utf-8 -*-
# @Time    : 2018/2/27 16:49
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : excel.py
# @Software: PyCharm Community Edition
import xlrd
from datetime import datetime,date
def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook(r'G:\github\UTT_python\test.xlsx')
    logininformation = workbook.sheet_by_name("登陆信息")
    # print(logininformation.cell(1,1).value)
    # print("sheet的名称:%s，行数:%s，列数:%s" % (logininformation.name,logininformation.nrows, logininformation.ncols))
    username = []
    for i in range(1,logininformation.nrows):
        name = logininformation.cell(i,0).value
        # print(name)
        username.append(name)
    print("用户名为：",username)
    password= []
    for i in range(1, logininformation.nrows):
        for j in range(1, logininformation.ncols):
            pwd = logininformation.cell(i, j).value
            # print(pwd)
            password.append(pwd)
    print("密码为：", password)
    # # 获取所有sheet
    # print("获取所有sheet",workbook.sheet_names())
    # # 根据sheet索引或者名称获取sheet内容
    # sheet2 =workbook.sheet_by_index(1)
    # # sheet的名称，行数，列数
    # print("sheet的名称:%s，行数:%s，列数:%s"%(sheet2.name,sheet2.nrows,sheet2.ncols))
    # # 获取整行和整列的值（数组）
    # rows = sheet2.row_values(1)
    # clos = sheet2.col_values(1)
    # print("整行的值：",rows,"整列的值",clos)
    # # 获取单元格内容
    # print(sheet2.cell(1,0).value)
    # print(sheet2.cell(2,0).value)

    # 获取单元格内容的数据类型
    # print(sheet2.cell(0,0).ctype)
    # for sheet_name in workbook.sheet_names():
    #     # print(workbook.sheet_names())
    #     sheet2 = workbook.sheet_by_name(sheet_name)
    #     print(sheet_name)
    #     rows = sheet2.row_values(1)
    #   # 获取第四行内容
    #     cols = sheet2.col_values(1)  # 获取第二列内容
    #     print(rows)
    #     print(cols)


if __name__ == '__main__':
    read_excel()