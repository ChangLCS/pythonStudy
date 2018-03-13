#! /usr/bin/env python
# -*- coding: utf-8 -*-
import time

import os  # 文件、目录模块
import sys

import xlrd  # 读取 excel
from selenium import webdriver  # python 启动浏览器
from threading import Timer  # 定时器

driver = webdriver.Chrome()  # 打开谷歌
# driver = webdriver.Ie()  # 打开IE

# Load page 在地址栏输入http://www.baidu.com 进入百度
driver.get("http://login.develop.wei3dian.com/login.html")

driver.maximize_window()

_form = driver.find_element_by_id('loginForm')

driver.find_element_by_id('loginId').clear()  # 先清除用户名
driver.find_element_by_id('loginId').send_keys(
    'LCS2018')  # 根据id找到对应的输入框  输入用户名

driver.find_element_by_id('password').clear()  # 先清除密码
driver.find_element_by_id('password').send_keys('123456')  # 根据id找到对应的输入框  输入密码

# 这里还要处理一下CA登录是否输入了密码

time.sleep(1)

driver.find_element_by_class_name(
    'login_box_r').click()  # 关掉ca登录
time.sleep(1)
driver.find_element_by_class_name('btn-block').click()  # 找到对应的按钮  登陆
time.sleep(1)

driver.find_element_by_class_name('fa-cubes').click()  # 找到对应的按钮  数据中心 进入系统
time.sleep(5)

_menu_first = driver.find_element_by_name('企业机构库')
_menu_first.click()
time.sleep(1)
_menu_first.find_element_by_name('生产企业').click()  # 找到 企业机构库》生产企业  点击
time.sleep(1)

_xlsx_path = os.path.join('docs', 'excel', '企业信息.xlsx')
_data = xlrd.open_workbook(_xlsx_path)

_table = _data.sheet_by_index(0)  # 通过索引获取excel的sheet

_nrows = _table.nrows
# _nrows = _table.row_values(1)

i = 0
while i < _nrows:
    if i > 0:
        __row = _table.row_values(i)  # 1, 生产企业， 生产， 广东省,深圳市,南山区
        print(__row)
        pass
    i += 1
    pass

print(_data)

time.sleep(5)

driver.quit()

# # 打开谷歌浏览器
# driver = webdriver.Ie()
# # driver = webdriver.Chrome(executable_path=path)
# # driver = webdriver.Ie(executable_path=path)
# # driver.get("http://trade.develop.wei3dian.com") # Load page 在地址栏输入http://www.baidu.com 进入百度
# # 定位元素的五中方式 id name xpath link class
# driver.get("http://login.develop.wei3dian.com/login.html")

# driver.find_element_by_id('loginId').clear()  # 先清除用户名
# driver.find_element_by_id('loginId').send_keys(
#     'dghmyy2018')  # 根据id找到对应的输入框  输入用户名dghmyy2018

# driver.find_element_by_id('password').clear()  # 先清除密码
# driver.find_element_by_id('password').send_keys(
#     'dghmyy2018')  # 根据id找到对应的输入框  输入密码dghmyy2018

# time.sleep(1)
# driver.find_element_by_class_name(
#     'login_box_r').click()  # 根据id找到对应的输入框  输入密码dghmyy2018
# time.sleep(2)
# driver.find_element_by_class_name('btn-block').click()  # 找到对应的按钮  登陆
# time.sleep(1)
# driver.find_element_by_class_name('fa-balance-scale').click()  # 找到对应的按钮  东莞交易
# time.sleep(3)
# driver.find_element_by_xpath(
#     '/html/body/div[2]/div/div/div[1]/div/div/div[2]/div[1]/div/ul/span[7]').click()  # 点击订单管理
# time.sleep(1)
# driver.find_element_by_xpath(
#     '/html/body/div[2]/div/div/div[1]/div/div/div[2]/div[1]/div/ul/span[7]/li/ul/li/ul/li[1]').click()  # 点击采购计划
# time.sleep(1)
# driver.find_element_by_class_name('page_left').click()  # 点击新增
# time.sleep(1)
# driver.find_element_by_xpath(
#     '/html/body/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/form/div/div[3]/div/div/div/button[1]/span').click()  # 点击添加明细
# time.sleep(1)
# # driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[4]/div/div/div/div[2]/div[2]/div[3]/table/tbody/tr[1]').click()  #选中一行
# driver.find_element_by_xpath(
#     '/html/body/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[4]/div/div/div/div[2]/div[2]/div[2]/table/thead/tr/th[1]/div/label/span').click()  # 全部选中
# time.sleep(1)
# driver.find_element_by_xpath(
#     '/html/body/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[4]/div/div/div/div[2]/div[3]/div/span/button[1]/span').click()  # 点击确认

# time.sleep(5)
# driver.quit()
