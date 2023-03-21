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
from utils import get_paddle_func, get_torch_func, get_torch_example, get_paddle_example
import webbrowser

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}

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

        web_get_button = QPushButton("打开api文档网站")
        grid.addWidget(web_get_button, 4, 0, 1, 1)
        web_get_button.clicked.connect(self.open_web)

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
        self.description = "两者功能一致。"
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
        btn4 = QRadioButton("仅 torch 参数更多")
        grid.addWidget(btn4, 7, 3, 1, 1)
        btn4.clicked.connect(lambda: self.setdifference(btn4.text()))
        btn5 = QRadioButton("仅 Paddle 参数更多")
        grid.addWidget(btn5, 8, 0, 1, 1)
        btn5.clicked.connect(lambda: self.setdifference(btn5.text()))
        btn6 = QRadioButton("参数用法不一致")
        grid.addWidget(btn6, 8, 1, 1, 1)
        btn6.clicked.connect(lambda: self.setdifference(btn6.text()))
        btn7 = QRadioButton("组合替代实现")
        grid.addWidget(btn7, 8, 2, 1, 1)
        btn7.clicked.connect(lambda: self.setdifference(btn7.text()))
        btn8 = QRadioButton("无参数且用法不一致")
        grid.addWidget(btn8, 8, 3, 1, 1)
        btn8.clicked.connect(lambda: self.setdifference(btn8.text()))

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setRowCount(2)
        self.table.setHorizontalHeaderLabels(['PyTorch', 'PaddlePaddle', '备注'])
        grid.addWidget(self.table, 9, 0, 3, 4)
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

        add_row_button = QPushButton("增加一行")
        grid.addWidget(add_row_button, 9, 4, 1, 1)
        f = lambda : self.table.insertRow(self.table.rowCount())
        add_row_button.clicked.connect(f)
        del_row_button = QPushButton("减少一行")
        grid.addWidget(del_row_button, 10, 4, 1, 1)
        f = lambda : self.table.removeRow(self.table.rowCount()-1)
        del_row_button.clicked.connect(f)

        # TODO add eval button to run example code
        grid.addWidget(QLabel('Torch Example', self), 12, 0, 1, 1)
        self.TorchExample = QTextEdit()
        grid.addWidget(self.TorchExample, 13, 0, 1, 5)
        self.TorchExample.setText('torch.abs(torch.tensor([-1, -2, 3]))')

        grid.addWidget(QLabel('Paddle Example', self), 14, 0, 1, 1)
        self.PaddleExample = QTextEdit()
        grid.addWidget(self.PaddleExample, 15, 0, 1, 5)
        self.PaddleExample.setText("import paddle\nx = paddle.to_tensor([-0.4, -0.2, 0.1, 0.3])\nout = paddle.abs(x)\nprint(out)")

        write_button = QPushButton("写文件")
        grid.addWidget(write_button, 16, 4, 1, 1)
        write_button.clicked.connect(self.write_md)

        self.setWindowTitle('test')
        self.show()

    def setdifference(self, text):
        self.difference = text
        diff2desp = {
            "无参数": "两者功能一致。",
            "参数完全一致": "两者功能一致且参数用法一致。",
            "仅参数名不一致": "两者功能一致且参数用法一致，仅参数名不一致，具体如下：",
            "仅 torch 参数更多": "其中 Paddle 相比 PyTorch 支持更多其他参数，具体如下：",
            "仅 Paddle 参数更多": "其中 PyTorch 相比 Paddle 支持更多其他参数，具体如下：",
            "参数用法不一致": "Paddle 和 PyTorch 的参数用法不一致，具体如下：",
            "组合替代实现": "PaddlePaddle 目前无对应 API，可使用如下代码组合实现该 API：",
            "无参数且用法不一致": "两者功能不完全一致，转写示例如下：",
        }
        self.description = diff2desp[self.difference]

    def getweb(self):
        try:
            torch_url = self.TorchUrl.text()
            torch_page = requests.get(torch_url, headers=headers).text
            if torch_page is None:
                print("输入pytorch网址错误，请重新输入！")
            else:
                torch_func = get_torch_func(torch_page)
                torch_example = get_torch_example(torch_page)
                self.TorchName.setText(torch_func)
                self.TorchExample.setText(torch_example)
        except Exception as e:
            print(e)

        try:
            paddle_url = self.PaddleUrl.text()
            paddle_page = requests.get(paddle_url, headers=headers).text
            if paddle_page is None:
                print("输入paddlepaddle网址错误，请重新输入！")
            else:
                paddle_func = get_paddle_func(paddle_page)
                paddle_example = get_paddle_example(paddle_page)
                self.PaddleName.setText(paddle_func)
                self.PaddleExample.setText(paddle_example)
        except Exception as e:
            print(e)

        # TODO 刷新表格的逻辑待补充
        # print(torch_page)

    def open_web(self):
        webbrowser.open_new_tab("https://www.paddlepaddle.org.cn/documentation/docs/zh/api/index_cn.html")
        webbrowser.open_new_tab("https://pytorch.org/docs/stable/index.html")

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
            f.write('{}\n\n'.format(self.description))
            if self.difference not in ['无参数', '参数完全一致', '组合替代实现', '无参数且用法不一致']:
                # write table
                f.write('### {}\n'.format('参数映射'))
                f.write('|PyTorch|PaddlePaddle|备注|\n')
                f.write('| ------- | ------- | ------- |\n')
                for i in range(self.table.rowCount()):
                    for j in range(self.table.columnCount()):
                        f.write('|{}'.format(self.table.item(i,j).text()))
                    f.write('|\n')
                f.write('\n')
            if self.difference not in ['无参数', '参数完全一致', '仅参数名不一致']:
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
