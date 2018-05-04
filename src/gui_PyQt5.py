#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication, QPushButton, QDesktopWidget, QTextBrowser)
from shopcart import main as shopcartMain


class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    # 提交数据事件
    def submitEvent(self):
        print(self.textEdit.toPlainText())
        ret = shopcartMain(self.textEdit.toPlainText())
        if ret == True:
            oldText = self.logText.toPlainText()
            newText = '\n----------%s----------\n%s\n%s' % (
                time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), self.textEdit.toPlainText(), oldText)
            self.logText.setText(newText)
            print('newText', newText)
        pass

    # 清楚文本框
    def cleanEvent(self):
        print(self.textEdit.toPlainText())
        self.textEdit.setText('')
        pass

    def initUI(self):
        # 扫码录入文本框
        text = QLabel('扫码录入')
        self.textEdit = QTextEdit()
        pass

        # 提交按钮
        submitbtn = QPushButton('提交数据', self)
        submitbtn.resize(submitbtn.sizeHint())
        submitbtn.clicked.connect(self.submitEvent)

        # 取消按钮
        cleanbtn = QPushButton('清楚现有数据', self)
        cleanbtn.resize(submitbtn.sizeHint())
        cleanbtn.clicked.connect(self.cleanEvent)

        # 文本历史
        log = QLabel('历史记录')
        self.logText = QTextEdit()

        # 创建布局
        grid = QGridLayout()
        grid.addWidget(text, 1, 0)
        grid.addWidget(self.textEdit, 1, 1, 1, 1)
        grid.addWidget(submitbtn, 2, 0)
        grid.addWidget(cleanbtn, 2, 1)
        grid.addWidget(log, 3, 0)
        grid.addWidget(self.logText, 3, 1, 5, 1)

        self.setLayout(grid)
        pass

        # resize()方法调整窗口的大小。这离是250px宽150px高
        self.resize(600, 500)
        # move()方法移动窗口在屏幕上的位置到x = 300，y = 300坐标。
        self.center()
        # 设置窗口的标题
        self.setWindowTitle('自动录单')
        # 显示在屏幕上
        self.show()
        pass

    # 控制窗口显示在屏幕中心的方法
    def center(self):
        # 获得窗口
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        pass


if __name__ == '__main__':
    # 每一pyqt5应用程序必须创建一个应用程序对象。sys.argv参数是一个列表，从命令行输入参数。
    app = QApplication(sys.argv)
    ex = AppWindow()

    # 系统exit()方法确保应用程序干净的退出
    # 的exec_()方法有下划线。因为执行是一个Python关键词。因此，exec_()代替
    sys.exit(app.exec_())
