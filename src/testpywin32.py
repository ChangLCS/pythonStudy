#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os  # 文件、目录模块
import sys
import xlrd  # 读取 excel
import webbrowser
from selenium import webdriver  # python 启动浏览器

import win32gui
import win32api
import win32con
import win32com.client

sys.path.insert(0, os.path.abspath(os.path.join(__file__, '../')))
from position import Pos


windows = {}  # 所有的窗口
win_id = 0  # 准备要操作的窗口id


# 获取窗口时候的回调
def find_window_callback(id, key):
    if win32gui.GetWindowText(id).strip():
        _item = []
        _item.append(hex(id))
        _item.append(win32gui.GetClassName(id))
        _item.append(win32gui.GetWindowText(id))
        if key == 'windows':
            windows[id] = _item
            pass
        pass


# 获取所有打开的窗口
win32gui.EnumWindows(find_window_callback, 'windows')

shell = win32com.client.Dispatch("WScript.Shell")
shell.SendKeys('%')

# 遍历一下，取到当前的
for item in windows:
    if '东莞交易' in windows[item][2]:
        print(windows[item])
        win_id = item
        print(win32gui.GetWindowRect(win_id))
        print(win32gui.GetWindowText(win_id))
        win32api.PostMessage(win_id, win32con.WM_SYSCOMMAND,
                             win32con.SC_MAXIMIZE, 0)
        print('-------------------------------------------------')
        win32gui.SetForegroundWindow(win_id)
        time.sleep(1)

        now_hWnd = win32gui.WindowFromPoint(
            (int(Pos.SCREEN_X/2), int(Pos.SCREEN_Y/2)))
        (Pos.now_hWnd_X1, Pos.now_hWnd_Y1, Pos.now_hWnd_X2,
         Pos.now_hWnd_Y2) = win32gui.GetWindowRect(now_hWnd)
        break
    pass


print('-------------------------------------------------')
print('-------------------------------------------------')
print(Pos.now_hWnd_X1)
print(Pos.now_hWnd_Y1)
print(Pos.now_hWnd_X2)
print(Pos.now_hWnd_Y2)
print(Pos.TJMX_X())
print(Pos.TJMX_Y())

win32api.SetCursorPos([Pos.TJMX_X(), Pos.TJMX_Y()])  # 设置鼠标位置
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 左键点击
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)  # 左键点击
