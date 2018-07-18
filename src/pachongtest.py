#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os  # 文件、目录模块
import sys

from pyquery import PyQuery as pq
from selenium import webdriver  # python 启动浏览器

import json
import re

tableELement = []
# dirlist = os.listdir(os.path.abspath(os.path.join(__file__, '../json')))


def getJSON(path):
    with open(path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        return data


def setHtml(index, pend):
    pList = driver.find_element_by_id('content').find_elements_by_tag_name('p')
    pList[index].click()
    time.sleep(1)

    # listmain = driver.find_element_by_class_name('listmain')
    pass


def goPage(index):
    if (index < endPage):
        goInt = tableELement.find_element_by_id('goInt')
        goInt.value(index)
        pageBtn = driver.find_element_by_css_selector(
            '#content > div:nth-child(1) > table:nth-child(4) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(8) > input:nth-child(1)')
        pageBtn.click()
        time.sleep(1)

        pList = driver.find_element_by_id(
            'content').find_elements_by_tag_name('p')
        pLen = len(pList)

        setHtml(0, pLen)
    else:
        print('已经到结束页了')


def do(path, name):
    driver.get(path)
    driver.implicitly_wait(1)
    _html = driver.find_element_by_tag_name('html')
    html = _html.get_attribute('innerHTML')
    if (html == '<head></head><body></body>'):
        time.sleep(1)
        do(path, name)
    else:
        filepath = os.path.abspath(os.path.join(
            __file__, '../html/', '%s%s' % (name, '.html')))
        myfile = open(filepath, 'w', encoding='utf-8')
        myfile.write(html)
        myfile.close()
        print(name)
        time.sleep(2)
    pass


if __name__ == '__main__':

    # for itemList in dirlist:
    #     itemPath = os.path.abspath(
    #         os.path.join(__file__, '../json/', itemList))
    #     itemjson = getJSON(itemPath)

    #     for item in itemjson:
    #         m = re.match(r"(.*)Id=(.*)", item['url'])
    #         print('item', item)
    #         if (m):
    #             id = m.group(2)
    #             do(item['url'], id)
    #         pass
    #     pass
    # main(json)
    driver = webdriver.Chrome(os.path.abspath('C:\\chromedriver.exe'))  # 打开谷歌
    driver.maximize_window()
    driver.get('http://app1.sfda.gov.cn/datasearch/face3/base.jsp?tableId=23&tableName=TABLE23&title=GMP%C8%CF%D6%A4&bcId=118715589530474392063703010776')
    time.sleep(1)

    tableList = driver.find_element_by_id(
        'ta3').find_elements_by_tag_name('table')
    for i in range(len(tableList)):
        print(i, tableList[i].text)
        pass

    module = input('选择爬取的模块')
    startpage = input('起始页')
    endPage = input('结束页')

    tableELement = tableList[int(module)]
    tableELement.click()
    pass

    goPage(startpage)
    pass
    print(__name__)
