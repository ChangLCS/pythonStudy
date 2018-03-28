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

import pythoncom
import pyHook   # 监听键盘或鼠标

assestpath = os.path.abspath(os.path.join(__file__, '../..'))  # 工程根目录
sys.path.insert(0, assestpath)
from position import Pos
from keyboard import JSON as KEYJSON

shell = win32com.client.Dispatch('WScript.Shell')


def DOUBLE_CLICK():
    # 双击事件，直接调用
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 左键点击
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)  # 左键点击
    pass
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 左键点击
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)  # 左键点击
    pass


def TAB_KEYUP():
    # 按TAB
    win32api.keybd_event(win32con.VK_TAB, 0, 0, 0)
    win32api.keybd_event(win32con.VK_TAB, 0, win32con.KEYEVENTF_KEYUP, 0)
    pass


def do_shopcart(xlsx_path=''):
    try:
        data = xlrd.open_workbook(xlsx_path)
        table = data.sheet_by_index(0)  # 通过索引获取excel的sheet
        nrows = table.nrows
        drug_code_index = 0
        drug_arr = []
        num_index = 0
        num_arr = []
        pass
    except Exception:
        return Exception

    i = 0
    while i < nrows:
        if i > 0:
            # 得出整条数据，并取药品编码
            row = table.row_values(i)
            if len(str(row[drug_code_index])) > 0 and len(str(row[num_index])) > 0:
                drug_arr.append(str(row[drug_code_index]))
                num_arr.append(str(row[num_index]))
                pass
        else:
            # 获得药品编码在哪一列
            drug_code_index = table.row_values(i).index('药品编码')
            # 获得订单数量在哪一列
            num_index = table.row_values(i).index('订单数量')
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
    shell.SendKeys('%')

    ishave_trade = False
    # 遍历一下，取到当前的
    for item in windows:
        if '东莞交易' in windows[item][2]:
            ishave_trade = True
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

    if ishave_trade == False:
        win32api.MessageBox(0, "没有找到交易平台", "error", win32con.MB_OK)
        return

    print('-------------------------------------------------')
    print('-------------------------------------------------')

    def find_drugs(code, num, index):
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
            win32api.keybd_event(
                KEYJSON[value], 0, win32con.KEYEVENTF_KEYUP, 0)
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
        win32api.SetCursorPos(
            [Pos.YPBMSSCHECK_X(), Pos.YPBMSSCHECK_Y()])  # 设置鼠标位置
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

        # 初始化tab焦点
        win32api.SetCursorPos([Pos.FIRSTDATA_X(), Pos.FIRSTDATA_Y()])  # 设置鼠标位置
        DOUBLE_CLICK()
        time.sleep(0.5)

        count = 0
        while count < index + 1:
            TAB_KEYUP()
            count += 1
            pass
        time.sleep(0.5)

        num_list = list(str(int(num)))
        for value in num_list:
            win32api.keybd_event(KEYJSON[value], 0, 0, 0)
            win32api.keybd_event(
                KEYJSON[value], 0, win32con.KEYEVENTF_KEYUP, 0)
            pass
        time.sleep(0.5)

        print(code, num)
        pass

    i = 0
    while i < len(drug_arr):
        find_drugs(drug_arr[i], float(num_arr[i]), i)
        i += 1
        pass


if __name__ == '__main__':
    print(__file__)
    _path = os.path.abspath(os.path.join(
        __file__, '..', 'docs', '订单明细目录.xls'))
    do_shopcart(_path)
