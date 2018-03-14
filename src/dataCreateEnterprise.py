#! /usr/bin/env python
# -*- coding: utf-8 -*-
import time

import os  # 文件、目录模块
import sys

import xlrd  # 读取 excel
from selenium import webdriver  # python 启动浏览器
from threading import Timer  # 定时器

from pywinauto import application  # C/S 软件操作

from docs.conf import Config

driver = webdriver.Chrome()  # 打开谷歌
# driver = webdriver.Ie()  # 打开IE

# Load page 在地址栏输入http://www.baidu.com 进入百度
driver.get(Config.assestpath)

driver.maximize_window()

form = driver.find_element_by_id('loginForm')

driver.find_element_by_id('loginId').clear()  # 先清除用户名
driver.find_element_by_id('loginId').send_keys(Config.username)  # 输入用户名

driver.find_element_by_id('password').clear()  # 先清除密码
driver.find_element_by_id('password').send_keys(Config.password)  # 输入密码

# 这里还要处理一下CA登录是否输入了密码

time.sleep(1)

driver.find_element_by_class_name('login_box_r').click()  # 关掉ca登录
time.sleep(1)
driver.find_element_by_class_name('btn-block').click()  # 找到对应的按钮  登陆
time.sleep(1)

driver.find_element_by_class_name('fa-cubes').click()  # 找到对应的按钮  数据中心 进入系统
time.sleep(5)

menu_first = driver.find_element_by_name('企业机构库')
menu_first.click()
time.sleep(1)
menu_first.find_element_by_name('生产企业').click()  # 找到 企业机构库》生产企业  点击
time.sleep(1)

xlsx_path = os.path.join('docs', 'excel', '企业信息.xlsx')
data = xlrd.open_workbook(xlsx_path)

table = data.sheet_by_index(0)  # 通过索引获取excel的sheet

nrows = table.nrows


def set_form_value(data):
    # 设置表单的value
    driver.find_element_by_name('create').click()
    time.sleep(1)
    pass
    fromtemp = driver.find_element_by_class_name('fromtemp')
    formitem_content = fromtemp.find_elements_by_class_name(
        'el-form-item__content')
    for item in formitem_content:
        try:
            _input = item.find_element_by_css_selector('input')
            _input.send_keys('你好啊')
            pass
        except Exception as error:  # 处理常规异常
            print(str(error))
            pass
        except BaseException as error:  # 所有异常基类
            print(str(error))
            pass
        pass
    time.sleep(1)
    pass


table_key = []


def get_table_json(row):
    # 获取excel每一行相对应的json
    i = 0
    json = {}
    while i < len(table_key):
        json[table_key[i]] = row[i]
        i += 1
        pass
    pass
    return json


i = 0
while i < nrows:
    if i > 0:
        row = table.row_values(i)  # 1, 生产企业， 生产， 广东省,深圳市,南山区
        data = get_table_json(row)
        set_form_value(data)
        pass
    else:
        table_key = table.row_values(i)
        pass
    i += 1
    pass

print(data)

time.sleep(5)

driver.quit()
