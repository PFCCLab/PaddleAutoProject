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
    QGridLayout, QFrame, QColorDialog, QLineEdit, QTableWidget, QTableWidgetItem, QRadioButton
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

        # grid.addWidget(QLabel('区别介绍', self), 7, 0, 1, 1)
        # self.Difference = QLineEdit("Torch参数更多")
        # grid.addWidget(self.Difference, 7, 1, 1, 4)

        self.difference = "无参数"
        btn1 = QRadioButton("无参数")
        btn1.setChecked(True)
        grid.addWidget(btn1, 7, 0, 1, 1)
        btn1.clicked.connect(lambda : self.setdifference(btn1.text()))
        btn2 = QRadioButton("参数完全一致")
        grid.addWidget(btn2, 7, 1, 1, 1)
        btn2.clicked.connect(lambda: self.setdifference(btn2.text()))
        btn3 = QRadioButton("仅参数名不一致")
        grid.addWidget(btn3, 7, 2, 1, 1)
        btn3.clicked.connect(lambda: self.setdifference(btn3.text()))
        btn4 = QRadioButton("torch 参数更多")
        grid.addWidget(btn4, 7, 3, 1, 1)
        btn4.clicked.connect(lambda: self.setdifference(btn4.text()))
        btn5 = QRadioButton("Paddle 参数更多")
        grid.addWidget(btn5, 8, 0, 1, 1)
        btn5.clicked.connect(lambda: self.setdifference(btn5.text()))
        btn6 = QRadioButton("参数不一致")
        grid.addWidget(btn6, 8, 1, 1, 1)
        btn6.clicked.connect(lambda: self.setdifference(btn6.text()))
        btn7 = QRadioButton("组合替代实现")
        grid.addWidget(btn7, 8, 2, 1, 1)
        btn7.clicked.connect(lambda: self.setdifference(btn7.text()))

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

        write_button = QPushButton("写文件")
        grid.addWidget(write_button, 14, 4, 1, 1)
        write_button.clicked.connect(self.write_md)

        self.setWindowTitle('test')
        self.show()

    def setdifference(self,text):
        self.difference[0] = text

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
        torch_name = self.TorchName.text().split('(')[0]
        paddle_name = self.PaddleName.text().split('(')[0]
        file_name = torch_name+'.md'
        with open(file_name,'w',encoding='utf-8') as f:
            # write head
            f.write('## [{}]{}\n\n'.format(self.difference,torch_name))
            # write torch
            f.write('### [{}]({})\n\n'.format(torch_name, self.TorchUrl.text()))
            f.write('```python\n{}\n```\n\n'.format(self.TorchName.text()))
            # write paddle
            f.write('### [{}]({})\n\n'.format(paddle_name, self.PaddleUrl.text()))
            f.write('```python\n{}\n```\n\n'.format(self.PaddleName.text()))
            # write introduction
            f.write('{}\n\n'.format(self.difference))
            # write table
            f.write('### {}\n'.format('参数映射'))
            f.write('|PyTorch|PaddlePaddle|备注|\n')
            f.write('| ------- | ------- | ------- |\n')
            for i in range(self.table.rowCount()):
                for j in range(self.table.columnCount()):
                    f.write('|{}'.format(self.table.item(i,j).text()))
                f.write('|\n')
            f.write('\n')
            # write code
            f.write('### {}\n\n'.format('转写示例'))
            f.write('```python\n')
            f.write('# Pytorch 写法\n')
            f.write(self.TorchExample.toPlainText())
            f.write('\n\n')
            f.write('# Paddle 写法\n')
            f.write(self.PaddleExample.toPlainText())
            f.write('\n')
            f.write('```\n')
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
