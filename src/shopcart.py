#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os  # 文件、目录模块
import sys
import xlrd  # 读取 excel
from selenium import webdriver  # python 启动浏览器
from threading import Timer  # 定时器

assestpath = os.path.abspath(os.path.join(__file__, '../..'))  # 工程根目录
sys.path.insert(0, assestpath)

from config import Config

# driver = webdriver.Chrome()  # 打开谷歌
driver = webdriver.Ie()  # 打开IE

# Load page 在地址栏输入http://www.baidu.com 进入百度
driver.get(Config.userurl)

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
pass

# 选择系统
link_ul = driver.find_element_by_class_name('link')
link_li = link_ul.find_elements_by_tag_name('li')

for item in link_li:
    if item.text == '东莞交易':
        item.click()
    pass
time.sleep(5)  # 等待时间长点，免得找不到购物车可以点
pass

# 进入购物车
driver.find_element_by_class_name('w_car_main').click()
time.sleep(2)
pass


xlsx_path = os.path.abspath(os.path.join(
    assestpath, 'docs', 'excel', '订单明细目录.xls'))
data = xlrd.open_workbook(xlsx_path)

table = data.sheet_by_index(0)  # 通过索引获取excel的sheet

nrows = table.nrows

table_index = 0
drug_arr = []
i = 0
while i < nrows:
    if i > 0:
        row = table.row_values(i)  # 1, 生产企业， 生产， 广东省,深圳市,南山区
        drug_arr.append(row[table_index])
        pass
    else:
        table_index = table.row_values(i).index('药品编码')
        pass
    i += 1
    pass


def find_drugs(code):
  # 查询药品编码
    driver.find_element_by_class_name('fromtrades').find_element_by_name(
        'isCreatShowTrade').click()  # 点击添加明细
    time.sleep(1)
    pass
    driver_input = driver.find_element_by_class_name('dialog-list').find_element_by_css_selector(
        'div[data-name=drugsCode]').find_element_by_tag_name('input')

    driver_input.clear()
    # 把code转list，一个一个send_key进去
    code_list = list(code)
    for value in code_list:
        driver_input.send_keys(value)
        pass

    time.sleep(1)
    pass
    driver.find_element_by_class_name(
        'dialog-list').find_element_by_name('dialogBtn').click()
    time.sleep(1)
    pass
    driver.find_element_by_class_name('dialog-list').find_element_by_tag_name(
        'thead').find_element_by_class_name('el-checkbox').click()
    time.sleep(1)
    pass
    driver.find_element_by_class_name(
        'dialog-list').find_element_by_name('isShowSure').click()
    time.sleep(1)
    pass
    print(code)
    pass


i = 0
while i < len(drug_arr):
    find_drugs(drug_arr[i])
    i += 1
    pass

# print(data)

# time.sleep(5)

# driver.quit()
