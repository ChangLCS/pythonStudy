#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os  # 文件、目录模块
import sys

from pyquery import PyQuery as pq
from selenium import webdriver  # python 启动浏览器

import json
import re


dirlist = os.listdir(os.path.abspath(os.path.join(__file__, '../json')))


def getJSON(path):
    with open(path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        return data


driver = webdriver.Chrome(os.path.abspath('C:\\chromedriver.exe'))  # 打开谷歌
driver.maximize_window()
time.sleep(1)


def do(path, name):
    driver.get(path)
    _html = driver.find_element_by_tag_name('html')
    html = _html.get_attribute('innerHTML')
    filepath = os.path.abspath(os.path.join(
        __file__, '../html/', '%s%s' % (name, '.html')))
    myfile = open(filepath, 'w', encoding='utf-8')
    myfile.write(html)
    myfile.close()
    print(name)
    time.sleep(2)
    pass


if __name__ == '__main__':

    for itemList in dirlist:
        itemPath = os.path.abspath(
            os.path.join(__file__, '../json/', itemList))
        json = getJSON(itemPath)

        for item in json:
            m = re.match(r"(.*)Id=(.*)", item['url'])
            if (m):
                id = m.group(2)
                do(item['url'], id)
            pass
        pass

    # main(json)
