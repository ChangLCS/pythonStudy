#! /usr/bin/env python
# -*- coding: utf-8 -*-

import win32api
import win32con


class Position:
    SCREEN_X = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    SCREEN_Y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)

    now_hWnd = 0  # 当前操作窗口 id
    now_hWnd_X1 = 0  # 当前操作窗口的坐标
    now_hWnd_Y1 = 0
    now_hWnd_X2 = 0
    now_hWnd_Y2 = 0

    def __init__(self):
        pass

    # 订单管理-订单购物车-添加明细按钮
    def TJMX_X(self):
        return int(self.now_hWnd_X1 + 330)

    def TJMX_Y(self):
        return int(self.now_hWnd_Y1 + 275)

    # 已知弹出框 width 90% top 15%
    # 订单管理-订单购物车-添加明细--药品编码搜索
    def YPBMSS_X(self):
        return int((self.now_hWnd_X2 - self.now_hWnd_X1) * 0.05 + self.now_hWnd_X1 + 170)

    def YPBMSS_Y(self):
        return int((self.now_hWnd_Y2 - self.now_hWnd_Y1) * 0.15 + self.now_hWnd_Y1 + 105)

    # 订单管理-订单购物车-添加明细--药品编码搜索按钮
    def YPBMSSBTN_X(self):
        return int(self.now_hWnd_X2 - self.now_hWnd_X1 - (self.now_hWnd_X2 - self.now_hWnd_X1) * 0.05 - 50)

    def YPBMSSBTN_Y(self):
        return int((self.now_hWnd_Y2 - self.now_hWnd_Y1) * 0.15 + self.now_hWnd_Y1 + 105)

    # 订单管理-订单购物车-添加明细--弹出框全选
    def YPBMSSCHECK_X(self):
        return int((self.now_hWnd_X2 - self.now_hWnd_X1) * 0.05 + self.now_hWnd_X1 + 40)

    def YPBMSSCHECK_Y(self):
        return int((self.now_hWnd_Y2 - self.now_hWnd_Y1) * 0.15 + self.now_hWnd_Y1 + 160)

    # 订单管理-订单购物车-添加明细--确定
    def SUREBTN_X(self):
        return int(self.now_hWnd_X2 - self.now_hWnd_X1 - (self.now_hWnd_X2 - self.now_hWnd_X1) * 0.05 - 150)

    def SUREBTN_Y(self):
        return int(self.now_hWnd_Y2 - (self.now_hWnd_Y2 - self.now_hWnd_Y1) * 0.15 - 50)


Pos = Position()

if __name__ == '__main__':
    print(__file__)
