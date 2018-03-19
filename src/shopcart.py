#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os  # 文件、目录模块
import sys
import xlrd  # 读取 excel

import win32gui
import win32api
import win32con
import win32com.client

assestpath = os.path.abspath(os.path.join(__file__, '../..'))  # 工程根目录
sys.path.insert(0, assestpath)
from position import Pos
from keyboard import JSON as KEYJSON


xlsx_path = os.path.abspath(os.path.join(
    assestpath, 'docs', 'excel', '订单明细目录.xls'))
data = xlrd.open_workbook(xlsx_path)

table = data.sheet_by_index(0)  # 通过索引获取excel的sheet

nrows = table.nrows

table_index = 0
drug_arr = []
i = 0
while i < nrows:
    if i > 0:
        # 得出整条数据，并取药品编码
        row = table.row_values(i)
        drug_arr.append(row[table_index])
        pass
    else:
        # 获得药品编码在那一列
        table_index = table.row_values(i).index('药品编码')
        pass
    i += 1
    pass


windows = {}  # 所有的窗口
win_id = 0  # 准备要操作的窗口id


def find_window_callback(id, key):
    # 获取窗口时候的回调
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
        win_id = item
        # 最大化
        win32api.PostMessage(win_id, win32con.WM_SYSCOMMAND,
                             win32con.SC_MAXIMIZE, 0)
        win32gui.SetForegroundWindow(win_id)
        time.sleep(1)

        Pos.now_hWnd = win32gui.WindowFromPoint(
            (int(Pos.SCREEN_X/2), int(Pos.SCREEN_Y/2)))
        (Pos.now_hWnd_X1, Pos.now_hWnd_Y1, Pos.now_hWnd_X2,
         Pos.now_hWnd_Y2) = win32gui.GetWindowRect(Pos.now_hWnd)
        break
    pass


print('-------------------------------------------------')
print('-------------------------------------------------')


def find_drugs(code):
    # 添加明细
    win32api.SetCursorPos([Pos.TJMX_X(), Pos.TJMX_Y()])  # 设置鼠标位置
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 左键点击
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)  # 左键点击
    time.sleep(1)
    pass

    # 药品编码搜索框
    win32api.SetCursorPos([Pos.YPBMSS_X(), Pos.YPBMSS_Y()])  # 设置鼠标位置
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 左键点击
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)  # 左键点击
    time.sleep(1)
    pass

    # 清空输入框原有参数
    win32api.keybd_event(win32con.VK_LCONTROL, 0, 0, 0)
    win32api.keybd_event(KEYJSON['A'], 0, 0, 0)
    win32api.keybd_event(KEYJSON['A'], 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(win32con.VK_LCONTROL, 0,
                         win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.2)
    pass

    # 把code转list，一个一个 输入进去
    code_list = list(code)
    for value in code_list:
        if value in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            win32api.keybd_event(win32con.VK_SHIFT, 0, 0, 0)
            pass
        win32api.keybd_event(KEYJSON[value], 0, 0, 0)
        win32api.keybd_event(KEYJSON[value], 0, win32con.KEYEVENTF_KEYUP, 0)
        if value in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            win32api.keybd_event(win32con.VK_SHIFT, 0,
                                 win32con.KEYEVENTF_KEYUP, 0)
            pass
        time.sleep(0.1)
        pass

    # 点击搜索按钮
    win32api.SetCursorPos([Pos.YPBMSSBTN_X(), Pos.YPBMSSBTN_Y()])  # 设置鼠标位置
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 左键点击
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)  # 左键点击
    time.sleep(1)
    pass

    # 全选订单明细
    win32api.SetCursorPos([Pos.YPBMSSCHECK_X(), Pos.YPBMSSCHECK_Y()])  # 设置鼠标位置
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 左键点击
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)  # 左键点击
    time.sleep(1)
    pass

    # 确定选中
    win32api.SetCursorPos([Pos.SUREBTN_X(), Pos.SUREBTN_Y()])  # 设置鼠标位置
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 左键点击
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)  # 左键点击
    time.sleep(1)
    pass

    print(code)
    pass


i = 0
while i < len(drug_arr):
    find_drugs(drug_arr[i])
    i += 1
    pass

# print(data)

# time.sleep(5)

# driver.quit()


if __name__ == '__main__':
    print(__file__)
