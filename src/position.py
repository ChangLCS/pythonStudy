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

    # 添加明细按钮位置
    def TJMX_SCREEN_POS(self):
        _X1 = int(self.now_hWnd_X1 + 280)
        _X2 = int(self.now_hWnd_X1 + 290)
        # _Y1 = int(self.now_hWnd_Y1 + 260) # 1.0
        # _Y2 = int(self.now_hWnd_Y1 + 270)
        _Y1 = int(self.now_hWnd_Y1 + 275)  # 2.0
        _Y2 = int(self.now_hWnd_Y1 + 280)
        return (_X1, _Y1, _X2, _Y2)

    # 第一条数据的位置
    def FIRSTDATA_X(self):
        # return int(self.now_hWnd_X1 + 420)
        return int(self.now_hWnd_X1 + 320)  # 2.0

    def FIRSTDATA_Y(self):
        return int(self.now_hWnd_Y1 + 340)

    # 已知弹出框 width 90% top 15%
    # 订单管理-订单购物车-添加明细--药品编码搜索
    def YPBMSS_X(self):
        # return int((self.now_hWnd_X2 - self.now_hWnd_X1) * 0.05 + self.now_hWnd_X1 + 170) # 1.0
        # 2.0
        return int((self.now_hWnd_X2 - self.now_hWnd_X1) * 0.075 + self.now_hWnd_X1 + 170)

    def YPBMSS_Y(self):
        return int((self.now_hWnd_Y2 - self.now_hWnd_Y1) * 0.15 + self.now_hWnd_Y1 + 105)

    # 订单管理-订单购物车-添加明细--药品编码搜索按钮
    def YPBMSSBTN_X(self):
        # return int(self.now_hWnd_X2 - self.now_hWnd_X1 - (self.now_hWnd_X2 - self.now_hWnd_X1) * 0.05 - 50) # 1.0
        # 2.0
        return int(self.now_hWnd_X2 - self.now_hWnd_X1 - (self.now_hWnd_X2 - self.now_hWnd_X1) * 0.075 - 50)

    def YPBMSSBTN_Y(self):
        return int((self.now_hWnd_Y2 - self.now_hWnd_Y1) * 0.15 + self.now_hWnd_Y1 + 105)

    # 订单管理-订单购物车-添加明细--弹出框全选
    def YPBMSSCHECK_X(self):
        # return int((self.now_hWnd_X2 - self.now_hWnd_X1) * 0.05 + self.now_hWnd_X1 + 40) # 1.0
        # 2.0
        return int((self.now_hWnd_X2 - self.now_hWnd_X1) * 0.075 + self.now_hWnd_X1 + 40)

    def YPBMSSCHECK_Y(self):
        return int((self.now_hWnd_Y2 - self.now_hWnd_Y1) * 0.15 + self.now_hWnd_Y1 + 160)

    # 订单管理-订单购物车-添加明细--确定
    def SUREBTN_X(self):
        # return int(self.now_hWnd_X2 - self.now_hWnd_X1 - (self.now_hWnd_X2 - self.now_hWnd_X1) * 0.05 - 150) # 1.0
        # 2.0
        return int(self.now_hWnd_X2 - self.now_hWnd_X1 - (self.now_hWnd_X2 - self.now_hWnd_X1) * 0.05 - 150)

    def SUREBTN_Y(self):
        return int(self.now_hWnd_Y2 - (self.now_hWnd_Y2 - self.now_hWnd_Y1) * 0.10 - 50)

    # 弹框列表第一条的选中按钮区域
    def SCREEN_IMAGE_POSITION(self):
        # 1.0
        # _X1 = int((self.now_hWnd_X2 - self.now_hWnd_X1)
        #           * 0.05 + self.now_hWnd_X1 + 24)
        # _X2 = int((self.now_hWnd_X2 - self.now_hWnd_X1)
        #           * 0.05 + self.now_hWnd_X1 + 54)
                  # 2.0
        _X1 = int((self.now_hWnd_X2 - self.now_hWnd_X1)
                  * 0.075 + self.now_hWnd_X1 + 24)
        _X2 = int((self.now_hWnd_X2 - self.now_hWnd_X1)
                  * 0.075 + self.now_hWnd_X1 + 54)
        _Y1 = int((self.now_hWnd_Y2 - self.now_hWnd_Y1)
                  * 0.15 + self.now_hWnd_Y1 + 180)
        _Y2 = int((self.now_hWnd_Y2 - self.now_hWnd_Y1)
                  * 0.15 + self.now_hWnd_Y1 + 200)
        return (_X1, _Y1, _X2, _Y2)


Pos = Position()

if __name__ == '__main__':
    print(__file__)
