#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

baseurl = os.path.join(__file__, '../..')
sys.path.insert(0, os.path.abspath(baseurl))

print(sys.path)

# print(os.path.abspath(''))

import world

print('hello')
