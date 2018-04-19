#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os  # 文件、目录模块
import sys

import win32gui
import win32api
import win32con
import win32com.client

from PIL import Image, ImageGrab

from pynput import keyboard  # 鼠标、键盘监听


assestpath = os.path.abspath(os.path.join(__file__, '../..'))  # 工程根目录
sys.path.insert(0, assestpath)
from position import Pos
from keyboard import JSON as KEYJSON

shell = win32com.client.Dispatch('WScript.Shell')

ishave_num = False


def on_press(key):
    pass


def on_release(key):
    if key == keyboard.Key.esc:
        os._exit(0)
        return False


def main():
    print('main')
    while True:
        with keyboard.Listener(on_press, on_release) as listener:
            print(__file__)
            _path = os.path.abspath(os.path.join(
                __file__, '..', 'docs', '订单明细目录.txt'))
            do_shopcart(_path)
            listener.join()


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


def do_shopcart(file_path=''):
    global ishave_num
    txt_data = []
    print('do_shopcart')
    try:
        txt = open(file_path)
        for item in txt:
            item_text = item.replace('\n', '').split('&')
            if not(len(item_text) == 1 and len(item_text[0]) == 0):
                txt_data.append(item_text)
                pass
        nrows = len(txt_data)
        txt.close()
        pass
    except Exception:
        return Exception
    print('txt_data', txt_data)

    i = 0
    drug_arr = []
    num_arr = []
    drug_code_index = 2  # 医院药品编码的位置索引
    num_index = 4  # 药品数量的位置索引
    while i < nrows:
        row = txt_data[i]
        print('row', row)
        if len(row) >= drug_code_index and len(row) >= num_index and len(str(row[drug_code_index])) > 0 and len(str(row[drug_code_index])) > 1 and len(str(row[num_index])) > 0 and row[num_index].isdigit():
            drug_arr.append(str(row[drug_code_index]))
            num_arr.append(str(row[num_index]))
            pass
        i += 1
        pass
    print('drug_arr', drug_arr)
    print('num_arr', num_arr)

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
        win32api.MessageBox(0, '没有找到交易平台', 'error', win32con.MB_OK)
        return

    print('-------------------------------------------------')
    print('-------------------------------------------------')

    def find_drugs(code, num, index):
        print(code, num, index)
        global ishave_num
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
        time.sleep(0.1)
        win32api.keybd_event(KEYJSON['A'], 0, 0, 0)
        time.sleep(0.1)
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
                time.sleep(0.1)
                pass
            win32api.keybd_event(KEYJSON[value], 0, 0, 0)
            time.sleep(0.1)
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

        img = ImageGrab.grab(Pos.SCREEN_IMAGE_POSITION())
        px = img.load()
        for x in range(img.width):
            for y in range(img.height):
                if (str(px[x, y]) != str((255, 255, 255))):
                    ishave_num = True
                    break
                pass
            pass

        # 确定选中
        win32api.SetCursorPos([Pos.SUREBTN_X(), Pos.SUREBTN_Y()])  # 设置鼠标位置
        win32api.mouse_event(
            win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 左键点击
        win32api.mouse_event(
            win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)  # 左键点击
        time.sleep(1)
        pass

        if ishave_num:
            # 初始化tab焦点
            win32api.SetCursorPos(
                [Pos.FIRSTDATA_X(), Pos.FIRSTDATA_Y()])  # 设置鼠标位置
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
    table_index = 0
    while i < len(drug_arr):
        ishave_num = False
        print('num_arr[i]', num_arr[i])
        find_drugs(drug_arr[i], float(num_arr[i]), table_index)
        if ishave_num:
            table_index += 1
        i += 1
        pass

    txt = open(file_path, 'w')
    txt.write('')
    txt.close()
    os._exit(0)


if __name__ == '__main__':
    main()
