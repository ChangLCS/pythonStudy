#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os  # 文件、目录模块
import sys
import xlrd  # 读取 excel
import webbrowser
from selenium import webdriver  # apython 启动浏览器

import win32gui
import win32api
import win32con
import win32com.client


windows = {}  # 所有的窗口
win_id = 0  # 准备要操作的窗口


# 获取窗口时候的回调
def find_window_callback(id, data):
    windows = data
    if win32gui.GetWindowText(id).strip():
        _item = []
        _item.append(hex(id))
        _item.append(win32gui.GetClassName(id))
        _item.append(win32gui.GetWindowText(id))
        windows[id] = _item
    pass


# 获取所有打开的窗口
win32gui.EnumWindows(find_window_callback, windows)

shell = win32com.client.Dispatch("WScript.Shell")
shell.SendKeys('%')

# 遍历一下，取到当前的
for item in windows:
    if '东莞交易' in windows[item][2]:
        print(windows[item])
        win_id = item
        win32gui.SetForegroundWindow(win_id)
        break
    pass

windows_child = {}  # 子信息
win_childid = 0  # 子窗口id


def find_window_child_callback(childid, data):
    windows_child = data
    _item = []
    _item.append(hex(childid))
    _item.append(win32gui.GetClassName(childid))
    _item.append(win32gui.GetWindowText(childid))
    windows_child[childid] = _item
    pass


win32gui.EnumChildWindows(win_id, find_window_child_callback, windows_child)
print(windows_child)
