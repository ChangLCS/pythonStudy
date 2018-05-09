#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os  # 文件、目录模块
import time
from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication, QPushButton, QDesktopWidget, QTextBrowser, QFileIconProvider)
from PyQt5.QtGui import (QIcon, QPixmap, QTextCursor, QCursor)
from PyQt5.QtCore import (QSize, Qt)
from shopcart import main as shopcartMain

import requests

placeholder = '请扫码录入并点击提交，'


class AppWindow(QWidget):
    global placeholder

    def __init__(self):
        super().__init__()
        self.initUI()

    # 提交数据事件
    def submitEvent(self):
        print(self.textEdit.toPlainText())
        if self.textEdit.toPlainText() == placeholder:
            ret = shopcartMain('')
        else:
            ret = shopcartMain(self.textEdit.toPlainText())
        if ret == True:
            oldText = self.logText.toPlainText()
            newText = '\n----------%s----------\n%s\n%s' % (
                time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), self.textEdit.toPlainText(), oldText)
            self.logText.setText(newText)
            print('newText', newText)
            self.textEdit.setText('')
        pass

    # 清除文本框
    def cleanEvent(self):
        print(self.textEdit.toPlainText())
        self.textEdit.setText('')
        pass

    # 清除历史数据
    def cleanlogEvent(self):
        self.logText.setText('')
        pass

    # 文本焦点
    def textEditFocusInEvent(self, event):
        self.textEdit.repaint()
        if (self.textEdit.toPlainText() == placeholder):
            self.textEdit.setText('')
            self.textEdit.setStyleSheet('color: #000;')
        pass

    # 文本焦点消失
    def textEditFocusOutEvent(self, event):
        if (len(self.textEdit.toPlainText()) == 0):
            self.textEdit.setText(placeholder)
            self.textEdit.setStyleSheet('color: #999;')
        pass

    def initUI(self):
        try:
            submitimgreq = requests.get(
                'https://raw.githubusercontent.com/ChangLCS/pythonStudy/develop/src/images/icon-submit.png')
            submitimg = QPixmap()
            submitimg.loadFromData(submitimgreq.content)
            iconSubmit = QIcon(submitimg)
            pass
        except Exception:
            iconSubmit = QIcon()
            print('iconSubmit 读取失败')
            pass
        pass

        try:
            closeimgreq = requests.get(
                'https://raw.githubusercontent.com/ChangLCS/pythonStudy/develop/src/images/icon-reload.png')
            closeimg = QPixmap()
            closeimg.loadFromData(closeimgreq.content)
            iconClose = QIcon(closeimg)
            pass
        except Exception:
            iconClose = QIcon()
            print('iconClose 读取失败')
            pass
        pass

        # 提交按钮
        submitbtn = QPushButton('提交数据', self)
        submitbtn.setFixedHeight(60)
        submitbtn.setStyleSheet(
            'font-size: 30px; font-weight: bold; border: 2px solid #333;')
        submitbtn.clicked.connect(self.submitEvent)
        submitbtn.setIcon(iconSubmit)
        submitbtn.setIconSize(QSize(40, 40))
        pass

        # 取消按钮
        cleanbtn = QPushButton(self)
        cleanbtn.resize(cleanbtn.sizeHint())
        cleanbtn.setStyleSheet('border: 1px solid #333;')
        cleanbtn.clicked.connect(self.cleanEvent)
        cleanbtn.setIcon(iconClose)
        cleanbtn.setIconSize(QSize(20, 20))
        pass

        # 清除历史数据按钮
        cleanlogbtn = QPushButton(self)
        cleanlogbtn.resize(cleanlogbtn.sizeHint())
        cleanlogbtn.setStyleSheet('border: 1px solid #333;')
        cleanlogbtn.clicked.connect(self.cleanlogEvent)
        cleanlogbtn.setIcon(iconClose)
        cleanlogbtn.setIconSize(QSize(20, 20))
        pass

        # 扫码录入文本框
        text = QLabel('扫码录入')
        text.setAlignment(Qt.AlignCenter)
        self.textEdit = QTextEdit()
        self.textEdit.setCursor(QCursor())
        # 测试光标问题
        self.textEdit.setCursor(QCursor())
        self.textEdit.setText(placeholder)
        self.textEdit.setStyleSheet('color: #999;')
        self.textEdit.focusInEvent = self.textEditFocusInEvent
        self.textEdit.focusOutEvent = self.textEditFocusOutEvent
        pass

        # 文本历史
        log = QLabel('历史记录')
        log.setAlignment(Qt.AlignCenter)
        self.logText = QTextEdit()
        self.logText.setReadOnly(True)
        pass

        # 创建布局
        # 一般情况下我们都是把某个窗口部件放进栅格布局的一个单元中，但窗口部件有时也可能会需要占用多个单元。这时就需要用到addWidget()方法的一个重载版本，原型如下：

        # void addWidget(QWidget *, int row, int column, int rowSpan, int columnSpan, Qt::Alignment = 0);

        # 这个单元将从row和column开始，扩展到rowSpan和columnSpan指定的倍数的行和列。如果rowSpan或columnSpan的值为-1，则窗口部件将扩展到布局的底部或者右边边缘处。
        grid = QGridLayout()
        grid.addWidget(text, 0, 0, 5, 2)
        grid.addWidget(self.textEdit, 0, 2, 6, 10)
        grid.addWidget(cleanbtn, 5, 0, 1, 2, Qt.AlignCenter)
        grid.addWidget(submitbtn, 6, 2, 2, 10)
        grid.addWidget(log, 8, 0, 4, 2)
        grid.addWidget(cleanlogbtn, 12, 0, 1, 2, Qt.AlignCenter)
        grid.addWidget(self.logText, 8, 2, 5, 10)
        pass

        self.setLayout(grid)
        pass

        # resize()方法调整窗口的大小。这离是250px宽150px高
        self.resize(600, 500)
        # move()方法移动窗口在屏幕上的位置到x = 300，y = 300坐标。
        self.center()
        # 设置窗口的标题
        self.setWindowTitle('自动录单系统')
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
    app.setActiveWindow(ex)

    # 系统exit()方法确保应用程序干净的退出
    # 的exec_()方法有下划线。因为执行是一个Python关键词。因此，exec_()代替
    sys.exit(app.exec_())
