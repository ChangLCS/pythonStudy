#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os  # 文件、目录模块
import time
from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication, QPushButton, QDesktopWidget, QTextBrowser, QFileIconProvider)
from PyQt5.QtGui import (QIcon)
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

    def initUI(self):
        # 扫码录入文本框
        text = QLabel('扫码录入')
        self.textEdit = QTextEdit()
        pass

        iconSubmit = QIcon(os.path.abspath(os.path.join(
            __file__, '..', 'images', 'icon-submit.png')))
        iconClose = QIcon(os.path.abspath(os.path.join(
            __file__, '..', 'images', 'icon-close.png')))

        # 提交按钮
        submitbtn = QPushButton('提交数据', self)
        submitbtn.resize(submitbtn.sizeHint())
        submitbtn.clicked.connect(self.submitEvent)
        submitbtn.setIcon(iconSubmit)

        # 取消按钮
        cleanbtn = QPushButton('清除现有数据', self)
        cleanbtn.resize(cleanbtn.sizeHint())
        cleanbtn.clicked.connect(self.cleanEvent)
        cleanbtn.setIcon(iconClose)

        # 清除历史数据按钮
        cleanlogbtn = QPushButton('清除历史数据', self)
        cleanlogbtn.resize(cleanlogbtn.sizeHint())
        cleanlogbtn.clicked.connect(self.cleanlogEvent)
        cleanlogbtn.setIcon(iconClose)

        # 文本历史
        log = QLabel('历史记录')
        self.logText = QTextEdit()
        self.logText.setReadOnly(True)

        # 创建布局
        # 一般情况下我们都是把某个窗口部件放进栅格布局的一个单元中，但窗口部件有时也可能会需要占用多个单元。这时就需要用到addWidget()方法的一个重载版本，原型如下：

        # void addWidget(QWidget *, int row, int column, int rowSpan, int columnSpan, Qt::Alignment = 0);

        # 这个单元将从row和column开始，扩展到rowSpan和columnSpan指定的倍数的行和列。如果rowSpan或columnSpan的值为-1，则窗口部件将扩展到布局的底部或者右边边缘处。
        grid = QGridLayout()
        grid.addWidget(text, 0, 0, 6, 2)
        grid.addWidget(self.textEdit, 0, 2, 6, 10)
        grid.addWidget(submitbtn, 6, 0, 1, 4)
        grid.addWidget(cleanbtn, 6, 4, 1, 4)
        grid.addWidget(cleanlogbtn, 6, 8, 1, 4)
        grid.addWidget(log, 7, 0, 6, 2)
        grid.addWidget(self.logText, 7, 2, 6, 10)

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
