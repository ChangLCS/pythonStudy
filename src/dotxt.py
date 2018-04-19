#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os  # 文件、目录模块
import sys

import docx


def main():
    print('main')
    print(__file__)
    _path = os.path.abspath(os.path.join(
        __file__, '..', 'docs', '订单明细目录.docx'))
    print('_path', _path)

    file = docx.Document(_path)
    print(file.paragraphs)


if __name__ == '__main__':
    main()
