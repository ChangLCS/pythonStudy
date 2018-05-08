#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os  # 文件、目录模块
import sys
import requests
from pyquery import PyQuery as pq
from selenium import webdriver  # python 启动浏览器

baseUrl = 'http://app1.sfda.gov.cn/datasearch/face3/base.jsp'

baseUrlParams = 'http://app1.sfda.gov.cn/datasearch/face3/base.jsp?tableId=34&tableName=TABLE34&title=%E8%8D%AF%E5%93%81%E7%94%9F%E4%BA%A7%E4%BC%81%E4%B8%9A&bcId=118103348874362715907884020353'

testurl = 'http://app1.sfda.gov.cn/datasearch/face3/content.jsp?tableId=34&tableName=TABLE34&tableView=%E9%91%BD%EE%88%9A%E6%90%A7%E9%90%A2%E7%86%B6%E9%AA%87%E6%B5%BC%E4%BD%B7%E7%AC%9F&Id=1206'


def main():
    # data = {
    #     'tableId': 34, 'tableName': 'TABLE34', 'title': '药品生产企业', 'bcId': '118103348874362715907884020353',
    # }
    # r = requests.get(testurl)
    # print('r', r)
    # doc = pq(baseUrl, data)
    # print('doc', doc)
    pass
    driver = webdriver.Chrome()  # 打开谷歌
    driver.get(baseUrlParams)
    # driver.get(testurl)
    driver.find_element_by_tag_name('body')
    driver.maximize_window()
    time.sleep(1)
    driver.get(testurl)

    # _content = driver.find_element_by_id('content')
    _content = driver.find_element_by_class_name('listmain')
    _arr = _content.find_elements_by_tag_name('a')

    _hrefarr = []
    for _item in _arr:
        print(_item)
        _href = _item.get_attribute('href')
        _innerHTML = _content.get_attribute('innerHTML')
        # 'javascript:commitForECMA(callbackC,"content.jsp?tableId=34&tableName=TABLE34&tableView=%E9%91%BD%EE%88%9A%E6%90%A7%E9%90%A2%E7%86%B6%E9%AA%87%E6%B5%BC%E4%BD%B7%E7%AC%9F&Id=1206",null)'
        _hrefarr.append(_href)
        pass
    pass


if __name__ == '__main__':
    main()
