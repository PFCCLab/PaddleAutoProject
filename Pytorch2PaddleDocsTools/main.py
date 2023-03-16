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
import sys
import math
import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QPushButton, QFileDialog, QLabel, QTextEdit, \
    QGridLayout, QFrame, QColorDialog, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QColor, QImage, QPixmap
import requests
from utils import get_paddle_func,get_torch_func

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QLabel('PyTorch API url', self), 2, 0, 1, 1)
        grid.addWidget(QLabel('PaddlePaddle API url', self), 3, 0, 1, 1)

        self.TorchUrl = QLineEdit("https://pytorch.org/docs/1.13/generated/torch.abs.html?highlight=abs#torch.abs")
        grid.addWidget(self.TorchUrl, 2, 1, 1, 4)
        self.PaddleUrl = QLineEdit("https://www.paddlepaddle.org.cn/documentation/docs/zh/api/paddle/abs_cn.html#abs")
        grid.addWidget(self.PaddleUrl, 3, 1, 1, 4)

        web_get_button = QPushButton("解析网页")
        grid.addWidget(web_get_button, 4, 4, 1, 1)
        web_get_button.clicked.connect(self.getweb)

        grid.addWidget(QLabel('PyTorch API name', self), 5, 0, 1, 1)
        grid.addWidget(QLabel('PaddlePaddle API name', self), 6, 0, 1, 1)

        self.TorchName = QLineEdit("torch.abs(input, *, out=None)")
        grid.addWidget(self.TorchName, 5, 1, 1, 4)
        self.PaddleName = QLineEdit("paddle.abs(x, name=None)")
        grid.addWidget(self.PaddleName, 6, 1, 1, 4)

        grid.addWidget(QLabel('区别介绍', self), 7, 0, 1, 1)
        self.Difference = QLineEdit("Torch参数更多")
        grid.addWidget(self.Difference, 7, 1, 1, 4)

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setRowCount(2)
        self.table.setHorizontalHeaderLabels(['PyTorch', 'PaddlePaddle', '备注'])
        grid.addWidget(self.table, 9, 0, 1, 5)
        # 表格内容示例
        item1 = QTableWidgetItem('input')
        self.table.setItem(0, 0, item1)
        item2 = QTableWidgetItem('x')
        self.table.setItem(0, 1, item2)
        item3 = QTableWidgetItem('输入的Tensor，仅参数名不同')
        self.table.setItem(0, 2, item3)
        item1 = QTableWidgetItem('out')
        self.table.setItem(1, 0, item1)
        item2 = QTableWidgetItem('')
        self.table.setItem(1, 1, item2)
        item3 = QTableWidgetItem('表示输出的Tensor，PaddlePaddle无此参数，需要进行转写。')
        self.table.setItem(1, 2, item3)

        grid.addWidget(QLabel('Torch Example', self), 10, 0, 1, 1)
        self.TorchExample = QTextEdit()
        grid.addWidget(self.TorchExample, 11, 0, 1, 5)
        self.TorchExample.setText('torch.abs(torch.tensor([-1, -2, 3]))')

        grid.addWidget(QLabel('Paddle Example', self), 12, 0, 1, 1)
        self.PaddleExample = QTextEdit()
        grid.addWidget(self.PaddleExample, 13, 0, 1, 5)
        self.PaddleExample.setText("import paddle\nx = paddle.to_tensor([-0.4, -0.2, 0.1, 0.3])\nout = paddle.abs(x)\nprint(out)")

        web_get_button = QPushButton("解析网页")
        grid.addWidget(web_get_button, 14, 4, 1, 1)
        web_get_button.clicked.connect(self.write_md)

        self.setWindowTitle('test')
        self.show()

    def getweb(self):
        try:
            torch_url = self.TorchUrl.text()
            torch_func = get_torch_func(torch_url)
            self.TorchName.setText(torch_func)
        except:
            pass

        try:
            paddle_url = self.PaddleUrl.text()
            paddle_func = get_paddle_func(paddle_url)
            self.PaddleName.setText(paddle_func)
        except:
            pass

        # TODO 刷新表格的逻辑待补充
        # print(torch_page)

    def write_md(self):
        print("请在此函数内补充对应的写文件逻辑")
        # TODO 汇集各个框体中的信息
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
