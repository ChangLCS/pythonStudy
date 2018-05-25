#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os  # 文件、目录模块
import sys

from pyquery import PyQuery as pq
from selenium import webdriver  # python 启动浏览器

import json
import re

jsonurl = os.path.abspath(os.path.join(__file__, '../docs/data.json'))


def getJSON():
    with open(jsonurl, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        return data


baseUrl = 'http://app1.sfda.gov.cn/datasearch/face3/'

testurl = 'http://app1.sfda.gov.cn/datasearch/face3/content.jsp?tableId=41&tableName=TABLE41&tableView=药品经营企业&Id=412884'


driver = webdriver.Chrome()  # 打开谷歌
driver.maximize_window()
time.sleep(1)


def do(name, path):
    driver.get('%s%s' % (baseUrl, path))
    _html = driver.find_element_by_tag_name('html')
    html = _html.get_attribute('innerHTML')
    filepath = os.path.abspath(os.path.join(
        __file__, '../html/', '%s%s' % (name, '.html')))
    myfile = open(filepath, 'w', encoding='utf-8')
    myfile.write(html)
    myfile.close()
    print(name)
    pass


if __name__ == '__main__':

    json = getJSON()

    for item in json:
        m = re.match(r"([^']*)'(.*)'([^']*)", item['url'])
        if (m):
            path = m.group(2)
            do(item['name'], path)
        pass

    # main(json)
