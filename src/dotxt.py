#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os  # 文件、目录模块
import sys


def main():
    print('main')
    print(__file__)
    _path = os.path.abspath(os.path.join(
        __file__, '..', 'docs', '订单明细目录.txt'))
    print('_path', _path)

    txt = open(_path)
    for item in txt:
        print('item', item)
        item_text = item.replace('\n', '').split('&')
        print('item_text', item_text)
        pass


if __name__ == '__main__':
    main()
