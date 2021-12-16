#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/16 18:31
# @Author  : Yiu
# @Site    : 
# @File    : tapUI.py
# @Software: PyCharm
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import qtawesome
from PyQt5.QtWidgets import *

class TabDemo(QTabWidget):
    def __init__(self, parent=None):
        super(TabDemo, self).__init__(parent)

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()

        self.addTab(self.tab1, "Tab 1")
        self.addTab(self.tab2, "Tab 2")
        self.addTab(self.tab3, "Tab 3")
        self.addTab(self.tab4, "Tab 4")
        self.addTab(self.tab5, "Tab 5")

        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        self.tab4UI()
        self.tab5UI()

        self.decorate()
        self.setWindowTitle("Tab 例子")

    def tab1UI(self):
        # 帧布局
        main_widget = QWidget()
        left_widget = QWidget()
        right_widget = QWidget()
        bottom_widget = QWidget()
        main_layout = QGridLayout()
        left_layout = QGridLayout()
        right_layout = QGridLayout()
        bottom_layout = QGridLayout()

        main_widget.setLayout(main_layout)
        left_widget.setLayout(left_layout)
        right_widget.setLayout(right_layout)
        bottom_widget.setLayout(bottom_layout)

        left_layout.addWidget(QLabel("发送方"), 0, 0, 1, 1)
        left_layout.addWidget(QLabel("IP："), 1, 0, 3, 1)
        read_line = QtWidgets.QLineEdit()
        read_line.setPlaceholderText('输入发送方IP.')
        left_layout.addWidget(read_line, 1, 1, 3, 3)
        left_layout.addWidget(QLabel("端口："), 4, 0, 3, 1)
        read_line_1 = QtWidgets.QLineEdit()
        read_line_1.setPlaceholderText('输入发送方端口.')
        left_layout.addWidget(read_line_1, 4, 1, 3, 3)

        right_layout.addWidget(QLabel("接收方"), 0, 0, 1, 1)
        right_layout.addWidget(QLabel("IP："), 1, 0, 3, 1)
        read_line_2 = QtWidgets.QLineEdit()
        read_line_2.setPlaceholderText('输入接收方IP.')
        right_layout.addWidget(read_line_2, 1, 1, 3, 3)
        right_layout.addWidget(QLabel("端口："), 4, 0, 3, 1)
        read_line_3 = QtWidgets.QLineEdit()
        read_line_3.setPlaceholderText('输入接收方端口.')
        right_layout.addWidget(read_line_3, 4, 1, 3, 3)

        bottom_buttom_1 = QPushButton("连接网络")
        bottom_buttom_1.setFixedSize(180, 60)
        bottom_buttom_2 = QPushButton("断开网络")
        bottom_buttom_2.setFixedSize(180, 60)
        bottom_layout.addWidget(bottom_buttom_1, 0, 0, 1, 1)
        bottom_layout.addWidget(bottom_buttom_2, 0, 1, 1, 1)

        main_layout.addWidget(left_widget, 0, 0, 3, 1)
        main_layout.addWidget(right_widget, 0, 1, 3, 1)
        main_layout.addWidget(bottom_widget, 3, 0, 1, 2)

        self.setTabText(0, "网络设置")
        # 在标签1中添加这个帧布局
        self.tab1.setLayout(main_layout)

    # 同理如上
    def tab2UI(self):
        layout = QFormLayout()
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton("男"))
        sex.addWidget(QRadioButton("女"))
        layout.addRow(QLabel("性别"), sex)
        layout.addRow("生日", QLineEdit())
        self.setTabText(1, "数据加密")
        self.tab2.setLayout(layout)

    def tab3UI(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel("科目"))
        layout.addWidget(QCheckBox("物理"))
        layout.addWidget(QCheckBox("高数"))
        self.setTabText(2, "密钥协商")
        self.tab4.setLayout(layout)

    def tab4UI(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel("科目"))
        layout.addWidget(QCheckBox("物理"))
        layout.addWidget(QCheckBox("高数"))
        self.setTabText(3, "网络通信(AES)")
        self.tab4.setLayout(layout)

    def tab5UI(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel("科目"))
        layout.addWidget(QCheckBox("物理"))
        layout.addWidget(QCheckBox("高数"))
        self.setTabText(4, "操作信息")
        self.tab5.setLayout(layout)

    def decorate(self):
        # self.setTabShape(QTabWidget.TabShape.Triangular)
        self.tab1.setStyleSheet(
            """
            QWidget{
                color:#black;
                font-size:20px;
                font-weight:100;
                padding-top: 2px;
                padding-bottom: 2px;
                padding-left: 2px;
                padding-right: 2px;
                border: 1px solid black;
                border-radius: 10px;
                font-family: "华文中宋";
                text-align: center;
            }
            QPushButton{
                background: gray;
                border: none;
            }
            QPushButton:pressed{
                font-size: 25px;
                background: green;
                font-weight: bold;
            }
            """
        )

        self.setStyleSheet(
            """
                QTabWidget::pane  
                {
                    top:20px;
                    border:none;
                }
                QTabBar{
                    font-size:16px;
                }
                QTabBar::tab	
                {
                    color:#333333;
                    background:transparent;
                    font-family:"华文中宋";
                    font-size:16px;
                    padding-left:-9px;
                    padding-right:-9px;
                    width:180px;
                    height:30px;
                    margin-left:0px;
                    margin-right:40px;
                }

                QTabBar::tab:selected, QTabBar::tab:hover
                {
                    color:red;
                    background:transparent;
                    font-family: "华文中宋";
                    font-size:18px;
                    border-bottom:2px solid red;
                    font-weight: bold;
                }

            """
        )