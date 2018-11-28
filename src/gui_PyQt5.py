#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os  # 文件、目录模块
import time
import qtawesome

from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication, QPushButton, QDesktopWidget, QTextBrowser, QFileIconProvider)
from PyQt5.QtGui import (QIcon, QPixmap, QTextCursor, QCursor, QFont, QColor)
from PyQt5.QtCore import (QSize, Qt)
from shopcart import main as shopcartMain

import requests

_placeholder = '请扫码录入并点击提交，'
_baseColor = '#91c1e4'
_fontFamily = QFont('Microsoft YaHei')


class AppWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    # 提交数据事件
    def submitEvent(self):
        print(self.input_text.toPlainText())
        if self.input_text.toPlainText() == _placeholder:
            ret = shopcartMain('')
        else:
            ret = shopcartMain(self.input_text.toPlainText())
        if ret == True:
            oldText = self.history_log.toPlainText()
            newText = '\n----------%s----------\n%s\n%s' % (
                time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), self.input_text.toPlainText(), oldText)
            self.history_log.setText(newText)
            print('newText', newText)
            self.input_text.setText('')
        pass

    # 清除文本框
    def cleanEvent(self):
        print(self.input_text.toPlainText())
        self.input_text.setText('')
        pass

    # 清除历史数据
    def cleanlogEvent(self):
        self.history_log.setText('')
        pass

    # 文本焦点
    def textEditFocusInEvent(self, event):
        self.input_text.repaint()
        if (self.input_text.toPlainText() == _placeholder):
            self.input_text.setText('')
            self.input_text.setStyleSheet('color: #000;')
        pass

    # 文本焦点消失
    def textEditFocusOutEvent(self, event):
        if (len(self.input_text.toPlainText()) == 0):
            self.input_text.setText(_placeholder)
            self.input_text.setStyleSheet('color: #999;')
        pass

    # 最小化事件
    def minEvent(self, event):
        self.showMinimized()
        pass

    # 关闭事件
    def closeEvent(self, event):
        self.close()
        pass

    def initUI(self):
        # 创建布局
        # 一般情况下我们都是把某个窗口部件放进栅格布局的一个单元中，但窗口部件有时也可能会需要占用多个单元。这时就需要用到addWidget()方法的一个重载版本，原型如下：

        # void addWidget(QWidget *, int row, int column, int rowSpan, int columnSpan, Qt::Alignment = 0);
        #                               Y,X,height,width

        # 这个单元将从row和column开始，扩展到rowSpan和columnSpan指定的倍数的行和列。如果rowSpan或columnSpan的值为-1，则窗口部件将扩展到布局的底部或者右边边缘处。

        self.setFixedSize(800, 600)

        # resize()方法调整窗口的大小。这离是250px宽150px高
        # self.resize(600, 500)
        # move()方法移动窗口在屏幕上的位置到x = 300，y = 300坐标。
        self.center()
        # 设置窗口的标题
        self.setWindowTitle('自动录单系统')
        # 显示在屏幕上
        self.show()
        pass

        self.main_widget = QWidget()  # 创建窗口主部件
        self.main_widget.setObjectName('main_widget')
        self.main_layout = QGridLayout()    # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局

        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.top_widget = QWidget()  # 自定义标题栏
        self.top_widget.setObjectName('top_widget')
        self.top_layout = QGridLayout()  # 创建头部输入框主部件的网格布局层
        self.top_widget.setLayout(self.top_layout)

        self.input_widget = QWidget()  # 头部输入框主部件
        self.input_widget.setObjectName('input_widget')
        self.input_layout = QGridLayout()  # 创建头部输入框主部件的网格布局层
        self.input_widget.setLayout(self.input_layout)  # 设置头部输入框主部件布局为网格

        self.history_widget = QWidget()  # 头部历史记录主部件
        self.history_widget.setObjectName('history_widget')
        self.history_layout = QGridLayout()  # 创建历史记录主部件的网格布局层
        self.history_widget.setLayout(self.history_layout)  # 设置历史记录主部件布局为网格

        # self.main_layout.addWidget(self.top_widget, 0, 0, 1, 12)
        self.main_layout.addWidget(self.input_widget, 0, 0, 12, 12)
        self.main_layout.addWidget(self.history_widget, 12, 0, 11, 12)

        # self.top_blank = QWidget()
        # self.top_blank.setObjectName('top_blank')
        # 头部按钮
        # self.top_min = QPushButton(
        #     qtawesome.icon('fa.minus', color=_baseColor), '')
        # self.top_min.setObjectName('top_min')
        # self.top_min.clicked.connect(self.minEvent)
        # self.top_close = QPushButton(
        #     qtawesome.icon('fa.close', color=_baseColor), '')
        # self.top_close.setObjectName('top_close')
        # self.top_close.clicked.connect(self.closeEvent)

        # self.top_layout.addWidget(self.top_blank, 0, 0, 1, 22)
        # self.top_layout.addWidget(self.top_min, 0, 23, 1, 1)
        # self.top_layout.addWidget(self.top_close, 0, 24, 1, 1)

        # input 各个组件
        self.input_label = QLabel('扫码录入')  # 扫码录入
        self.input_label.setObjectName('input_label')

        self.input_clean = QPushButton(
            qtawesome.icon('fa.rotate-left', color=_baseColor), '')  # 清空输入框
        self.input_clean.setIconSize(QSize(28, 28))
        self.input_clean.setObjectName('input_clean')
        self.input_clean.clicked.connect(self.cleanEvent)

        self.input_text = QTextEdit()  # 输入框
        self.input_text.setObjectName('input_text')
        # self.input_text.setTextColor(QColor('#999'))
        self.input_text.setText(_placeholder)
        self.input_text.focusInEvent = self.textEditFocusInEvent
        self.input_text.focusOutEvent = self.textEditFocusOutEvent

        self.input_submit = QPushButton(qtawesome.icon(
            'fa.check-circle', color=_baseColor), '提交数据')   # 提交框
        self.input_submit.setIconSize(QSize(32, 32))
        self.input_submit.setFont(_fontFamily)
        self.input_submit.setObjectName('input_submit')
        self.input_submit.clicked.connect(self.submitEvent)

        self.input_layout.addWidget(self.input_label, 1, 0, 1, 3)
        self.input_layout.addWidget(self.input_clean, 2, 0, 2, 3)
        self.input_layout.addWidget(self.input_text, 0, 3, 9, 9)
        self.input_layout.addWidget(self.input_submit, 9, 3, 3, 9)
        pass

        # 历史记录
        self.history_label = QLabel('历史记录')  # 历史记录
        self.history_label.setObjectName('history_label')

        self.history_clean = QPushButton(
            qtawesome.icon('fa.rotate-left', color=_baseColor), '')  # 清空历史记录
        self.history_clean.setIconSize(QSize(28, 28))
        self.history_clean.setObjectName('history_clean')
        self.history_clean.clicked.connect(self.cleanlogEvent)

        self.history_log = QTextEdit()  # 历史记录日志
        self.history_log.setReadOnly(True)
        self.history_log.setObjectName('history_log')

        self.history_layout.addWidget(self.history_label, 1, 0, 1, 3)
        self.history_layout.addWidget(self.history_clean, 2, 0, 1, 3)
        self.history_layout.addWidget(self.history_log, 0, 3, 9, 9)
        pass

        self.top_widget.setStyleSheet('''
#top_widget {
    background-color: #f3f7fe;
}

#top_min {
    background: none;
    border: none;
}

#top_close {
    background: none;
    border: none;
}
''')

        self.input_label.setFixedWidth(160)
        self.input_label.setFixedHeight(33)
        self.input_label.setFont(_fontFamily)
        self.input_label.setAlignment(Qt.AlignCenter)
        self.input_widget.setStyleSheet('''
#input_widget {
    background-color: #f3f7fe;
}

#input_label {
    background-color: #91c1e4;
    color: #ffffff;
    font-size: 18px;
    border-radius: 10px;
    margin-left: 40px;
    text-align: center;
}

#input_clean {
    border: none;
    background: none;
}

#input_text {
    background-color: #ffffff;
    border: 1px solid #91c1e4;
    border-radius: 10px;
    padding: 10px;
    font-size: 14px;
}

#input_submit {
    background-color: #ffffff;
    border: 1px solid #91c1e4;
    font-size: 20px;
    height: 60px;
    border-radius: 30px;
}
''')

        self.history_label.setFixedWidth(160)
        self.history_label.setFixedHeight(33)
        self.history_label.setFont(_fontFamily)
        self.history_label.setAlignment(Qt.AlignCenter)
        self.history_widget.setStyleSheet('''
#history_widget {
    background-color: #f3f7fe;
}

#history_label {
    border: 1px solid #91c1e4;
    background-color: #ffffff;
    color: #666666;
    font-size: 18px;
    border-radius: 10px;
    margin-left: 40px;
    text-align: center;
}

#history_clean {
    border: none;
    background: none;
}

#history_log {
    background-color: #ffffff;
    border: 1px solid #91c1e4;
    border-radius: 10px;
    padding: 10px;
    font-size: 14px;
}
''')

        self.main_widget.setStyleSheet('''
#main_widget {
    border-radius: 10px;
    border: 2px solid #91c1e4;
}
''')

        self.setLayout(self.main_layout)
        pass

        # self.setWindowOpacity(0.9)
        # self.setAutoFillBackground(False)
        # self.setWindowFlag(Qt.FramelessWindowHint)  # 隐藏边框
        # self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明

        self.main_layout.setSpacing(0)
        pass

        pass

        # self.setLayout(self.main_layout)
        # pass

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
