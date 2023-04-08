#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Thanks to
https://blog.csdn.net/u014453898/article/details/88083173
https://github.com/maicss/PyQt-Chinese-tutorial
https://maicss.gitbooks.io/pyqt5/content/
zetcode.com
"""
import copy
import os
import math
import numpy as np
import sys
import cv2
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QPushButton, QFileDialog, QLabel, QTextEdit, \
    QGridLayout, QFrame, QColorDialog, QLineEdit, QTableWidget, QTableWidgetItem, QRadioButton
from PyQt5.QtCore import QTimer, Qt, QRect
from PyQt5.QtGui import QColor, QImage, QPixmap
import requests
import webbrowser
import re
from paddleocr import PaddleOCR, draw_ocr
import pyautogui
import pyperclip

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.run_flag = False

        self.initModel()
        self.initClock()
        self.initUI()

        self.fff = 1


    def initUI(self):

        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QLabel('聊天框', self), 1, 0, 1, 1)
        grid.addWidget(QLabel('xmin', self), 1, 1, 1, 1)
        grid.addWidget(QLabel('ymin', self), 1, 3, 1, 1)
        grid.addWidget(QLabel('xlen', self), 1, 5, 1, 1)
        grid.addWidget(QLabel('ylen', self), 1, 7, 1, 1)
        self.chatbox_xmin = QLineEdit("1000")
        self.chatbox_ymin = QLineEdit("500")
        self.chatbox_xlen = QLineEdit("400")
        self.chatbox_ylen = QLineEdit("40")
        grid.addWidget(self.chatbox_xmin, 1, 2, 1, 1)
        grid.addWidget(self.chatbox_ymin, 1, 4, 1, 1)
        grid.addWidget(self.chatbox_xlen, 1, 6, 1, 1)
        grid.addWidget(self.chatbox_ylen, 1, 8, 1, 1)

        grid.addWidget(QLabel('文字框', self), 2, 0, 1, 1)
        grid.addWidget(QLabel('xmin', self), 2, 1, 1, 1)
        grid.addWidget(QLabel('ymin', self), 2, 3, 1, 1)
        grid.addWidget(QLabel('xlen', self), 2, 5, 1, 1)
        grid.addWidget(QLabel('ylen', self), 2, 7, 1, 1)
        self.writebox_xmin = QLineEdit("1000")
        self.writebox_ymin = QLineEdit("580")
        self.writebox_xlen = QLineEdit("400")
        self.writebox_ylen = QLineEdit("50")
        grid.addWidget(self.writebox_xmin, 2, 2, 1, 1)
        grid.addWidget(self.writebox_ymin, 2, 4, 1, 1)
        grid.addWidget(self.writebox_xlen, 2, 6, 1, 1)
        grid.addWidget(self.writebox_ylen, 2, 8, 1, 1)

        button = QPushButton("检查区域")
        grid.addWidget(button, 3, 4, 1, 1)
        button.clicked.connect(self.check_cut_img)

        button = QPushButton("识别测试")
        grid.addWidget(button, 3, 6, 1, 1)
        button.clicked.connect(self.check_ocr)

        button = QPushButton("开启监听")
        grid.addWidget(button, 3, 8, 1, 1)
        button.clicked.connect(self.run_program)

        self.chatbox = QLabel()  # 定义显示视频的Label
        self.chatbox.setFixedSize(600, 200)
        grid.addWidget(self.chatbox, 4, 0, 1, 9)

        self.writebox = QLabel()  # 定义显示视频的Label
        self.writebox.setFixedSize(600, 200)
        grid.addWidget(self.writebox, 5, 0, 1, 9)

        self.setWindowTitle('WeChatBot')
        self.show()

    def initClock(self):
        # 通过定时器读取数据
        self.flush_clock = QTimer()  # 定义定时器，用于控制显示视频的帧率
        self.flush_clock.start(30)   # 定时器开始计时30ms，结果是每过30ms从摄像头中取一帧显示
        self.flush_clock.timeout.connect(self.check_frame)  # 若定时器结束，show_frame()

    def initModel(self):
        self.ocr = PaddleOCR(use_angle_cls=True, lang="ch",
                        threshold=0.5)  # need to run only once to download and load model into memory

    def check_cut_img(self):
        self.chatrect = QRect(int(self.chatbox_xmin.text()),
                              int(self.chatbox_ymin.text()),
                              int(self.chatbox_xlen.text()),
                              int(self.chatbox_ylen.text()))
        self.writerect = QRect(int(self.writebox_xmin.text()),
                               int(self.writebox_ymin.text()),
                               int(self.writebox_xlen.text()),
                               int(self.writebox_ylen.text()))
        self.writex = int(self.writebox_xmin.text()) + int(int(self.writebox_xlen.text())/2)
        self.writey = int(self.writebox_ymin.text()) + int(int(self.writebox_ylen.text())/2)

        # 屏幕截图
        screenshot = QApplication.primaryScreen().grabWindow(QApplication.desktop().winId())

        # 裁剪，保存，展示
        chatimg = screenshot.copy(self.chatrect)
        chatimg.save('now_img.jpg', format='JPG', quality=100)
        img = cv2.imread('now_img.jpg')
        img = cv2.resize(img, (600, 200))  # 把读到的帧的大小重新设置为 640x480
        showPic = QImage(img, img.shape[1], img.shape[0], QImage.Format_BGR888)
        self.chatbox.setPixmap(QPixmap.fromImage(showPic))

        writeimg = screenshot.copy(self.writerect)
        writeimg.save('write_img.jpg', format='JPG', quality=100)
        img = cv2.imread('write_img.jpg')
        img = cv2.resize(img, (600, 200))  # 把读到的帧的大小重新设置为 640x480
        showPic = QImage(img, img.shape[1], img.shape[0], QImage.Format_BGR888)
        self.writebox.setPixmap(QPixmap.fromImage(showPic))


    def check_ocr(self):
        img_path = 'now_img.jpg'
        img = cv2.imread(img_path)
        result = self.ocr.ocr(img, cls=True)

        # 输出结果
        s = ""
        for idx in range(len(result)):
            res = result[idx]
            for line in res:
                # print(line)
                s += line[1][0]
        print(s)

    def run_program(self):
        self.run_flag = True

    def check_frame(self):
        if self.run_flag:
            screenshot = QApplication.primaryScreen().grabWindow(QApplication.desktop().winId())

            # 裁剪，保存，展示
            chatimg = screenshot.copy(self.chatrect)
            chatimg.save('now_img.jpg', format='JPG', quality=100)
            img = cv2.imread('now_img.jpg')
            img = cv2.resize(img, (600, 200))  # 把读到的帧的大小重新设置为 640x480
            showPic = QImage(img, img.shape[1], img.shape[0], QImage.Format_BGR888)
            self.chatbox.setPixmap(QPixmap.fromImage(showPic))

            now_img = cv2.imread('now_img.jpg')
            # pre_img = cv2.imread('pre_img.jpg')
            result = self.ocr.ocr(now_img, cls=True)

            # difference = cv2.subtract(now_img, pre_img)

            #TODO: 判断相似度，以决定是否需要进行ocr

            # ocr
            # 获得结果
            s = ""
            for idx in range(len(result)):
                res = result[idx]
                for line in res:
                    s += line[1][0]
            # print(s)



            if 1: # self.fff == 1:
                if 'AAAA' in s:
                    pyautogui.moveTo(self.writex, self.writey, duration=0.25)
                    pyautogui.doubleClick()

                    pyperclip.copy("敏师傅快去提PR！")  # 复制
                    pyautogui.hotkey('ctrl', 'v')  # 粘贴
                    pyautogui.hotkey('Enter') # 发送

                    self.fff = 0

            # 保存上周期图片
            # img = cv2.imwrite('pre_img.jpg', now_img)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
