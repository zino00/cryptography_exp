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

    def Tbutton_1(self):
        self.pushbutton_1.setText(self.algrithm_1.text())
    def Tbutton_2(self):
        self.pushbutton_1.setText(self.algrithm_2.text())
    def Tbutton_3(self):
        self.pushbutton_1.setText(self.algrithm_3.text())
    def Tbutton_4(self):
        self.pushbutton_1.setText(self.algrithm_4.text())


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

        label_1 = QLabel("发送方")
        label_1.setStyleSheet(
            """
            border:none;
            border-bottom: 3px solid black;
            font-weight:700;
            background: transparent; 
            border-radius:0px;
            font-size:30px;
            padding:2px 4px;
            """)
        label_1.setFixedSize(140, 50)
        left_layout.addWidget(label_1, 0, 2, 1, 1)
        label_2 = QLabel("IP:")
        label_2.setStyleSheet("""border: none;background: #e3c56e""")
        label_2.setFixedSize(75, 50)
        left_layout.addWidget(label_2, 1, 0, 1, 1)
        read_line = QtWidgets.QLineEdit()
        read_line.setPlaceholderText('输入发送方IP.')
        left_layout.addWidget(read_line, 1, 1, 1, 4)
        label_3 = QLabel("端口:")
        label_3.setStyleSheet("""border: none;background: #e26073""")
        label_3.setFixedSize(75, 50)
        left_layout.addWidget(label_3, 2, 0, 1, 1)
        read_line_1 = QtWidgets.QLineEdit()
        read_line_1.setPlaceholderText('输入发送方端口.')
        left_layout.addWidget(read_line_1, 2, 1, 1, 4)

        label_4 = QLabel("接收方")
        label_4.setStyleSheet(
            """
            border:none;
            border-bottom: 3px solid black;
            font-weight:700;
            background: transparent; 
            border-radius:0px;
            font-size:30px;
            padding:2px 4px;
            """)
        label_4.setFixedSize(140, 50)
        right_layout.addWidget(label_4, 0, 2, 1, 1)
        label_5 = QLabel("IP:")
        label_5.setStyleSheet("""border: none;background: #e3c56e""")
        label_5.setFixedSize(75, 50)
        right_layout.addWidget(label_5, 1, 0, 1, 1)
        read_line_2 = QtWidgets.QLineEdit()
        read_line_2.setPlaceholderText('输入接收方IP.')
        right_layout.addWidget(read_line_2, 1, 1, 1, 4)
        label_6 = QLabel("端口:")
        label_6.setStyleSheet("""border: none;background: #e26073""")
        label_6.setFixedSize(75, 50)
        right_layout.addWidget(label_6, 2, 0, 1, 1)
        read_line_3 = QtWidgets.QLineEdit()
        read_line_3.setPlaceholderText('输入接收方端口.')
        right_layout.addWidget(read_line_3, 2, 1, 1, 4)

        label_1.setAlignment(QtCore.Qt.AlignCenter)
        label_2.setAlignment(QtCore.Qt.AlignCenter)
        label_3.setAlignment(QtCore.Qt.AlignCenter)
        label_4.setAlignment(QtCore.Qt.AlignCenter)
        label_5.setAlignment(QtCore.Qt.AlignCenter)
        label_6.setAlignment(QtCore.Qt.AlignCenter)

        bottom_buttom_1 = QPushButton("连接网络")
        bottom_buttom_1.setFixedSize(180, 60)
        bottom_buttom_1.setStyleSheet(
            """
            QPushButton{
                color: white;
                background: #17a05d;
                border: none;
            }
            QPushButton:pressed{
                background: #8f5b11;
                font-weight: bold;
            }
            """
        )
        bottom_buttom_2 = QPushButton("断开网络")
        bottom_buttom_2.setFixedSize(180, 60)
        bottom_buttom_2.setStyleSheet(
            """
            QPushButton{
                color: white;
                background: #c75450;
                border: none;
            }
            QPushButton:pressed{
                background: #8f5b11;
                font-weight: bold;
            }
            """
        )
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
        main_widget = QtWidgets.QWidget()
        main_layout = QtWidgets.QVBoxLayout()
        main_widget.setLayout(main_layout)

        pushbutton_widget = QtWidgets.QWidget()
        pushbutton_layout = QtWidgets.QGridLayout()
        pushbutton_widget.setLayout(pushbutton_layout)
        self.pushbutton_1 = QtWidgets.QLabel("请选择加密模式")
        self.pushbutton_1.setFixedSize(256, 50)
        self.pushbutton_1.setStyleSheet(
            """
           border:none;
            border-bottom: 3px solid black;
            font-weight:700;
            background: transparent; 
            border-radius:0px;
            font-size:30px;
            padding:2px 4px;
            """
        )
        self.pushbutton_1.setAlignment(QtCore.Qt.AlignCenter)
        pushbutton_layout.addWidget(self.pushbutton_1, 0, 0, 1, 1)
        main_layout.addWidget(pushbutton_widget)

        algrithm_widget = QtWidgets.QWidget()
        algrithm_layout = QtWidgets.QGridLayout()
        algrithm_widget.setLayout(algrithm_layout)

        self.algrithm_1 = QtWidgets.QToolButton()
        self.algrithm_1.setText("仿射加密")
        self.algrithm_1.setIcon(QtGui.QIcon('./assets/20210801.jpg'))
        self.algrithm_1.setIconSize(QtCore.QSize(200, 100))
        self.algrithm_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.algrithm_2 = QtWidgets.QToolButton()
        self.algrithm_2.setText("流密码加密")
        self.algrithm_2.setIcon(QtGui.QIcon('./assets/2021729_3.jpg'))
        self.algrithm_2.setIconSize(QtCore.QSize(200, 100))
        self.algrithm_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.algrithm_3 = QtWidgets.QToolButton()
        self.algrithm_3.setText("对称加密")
        self.algrithm_3.setIcon(QtGui.QIcon('./assets/bomb.jpeg'))
        self.algrithm_3.setIconSize(QtCore.QSize(200, 100))
        self.algrithm_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.algrithm_4 = QtWidgets.QToolButton()
        self.algrithm_4.setText("非对称加密")
        self.algrithm_4.setIcon(QtGui.QIcon('./assets/Leecode4.jpg'))
        self.algrithm_4.setIconSize(QtCore.QSize(200, 100))
        self.algrithm_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        algrithm_layout.addWidget(self.algrithm_1, 0, 0, 3, 1)
        algrithm_layout.addWidget(self.algrithm_2, 0, 1, 3, 1)
        algrithm_layout.addWidget(self.algrithm_3, 0, 2, 3, 1)
        algrithm_layout.addWidget(self.algrithm_4, 0, 3, 3, 1)

        self.algrithm_1.clicked.connect(self.Tbutton_1)
        self.algrithm_2.clicked.connect(self.Tbutton_2)
        self.algrithm_3.clicked.connect(self.Tbutton_3)
        self.algrithm_4.clicked.connect(self.Tbutton_4)

        algrithm_widget.setStyleSheet(
            """
            QToolButton{
                border:none;
            }
            QToolButton:hover{
                font-weight:bold;
            }
            QToolButton:pressed{
                border-bottom: 2px solid black;
            }
            """
        )

        main_layout.addWidget(algrithm_widget)

        passwd_1 = QtWidgets.QPushButton(qtawesome.icon('ei.twitter', color='black'), "明文")
        passwd_2 = QtWidgets.QPushButton(qtawesome.icon('fa.android', color='black'), "密文")
        passwd_3 = QtWidgets.QPushButton(qtawesome.icon('fa.apple', color='black'), "密钥配置")
        passwd_text_1 = QtWidgets.QTextEdit()
        passwd_text_2 = QtWidgets.QTextEdit()
        passwd_text_3 = QtWidgets.QTextEdit()
        passwd_1.setIconSize(QtCore.QSize(20, 20))
        passwd_2.setIconSize(QtCore.QSize(20, 20))
        passwd_3.setIconSize(QtCore.QSize(20, 20))

        passwd_widget = QtWidgets.QWidget()
        passwd_layout = QtWidgets.QGridLayout()
        passwd_widget.setLayout(passwd_layout)

        passwd_layout.addWidget(passwd_1, 0, 0, 1, 1)
        passwd_layout.addWidget(passwd_2, 0, 1, 1, 1)
        passwd_layout.addWidget(passwd_3, 0, 2, 1, 1)
        passwd_layout.addWidget(passwd_text_1, 1, 0, 3, 1)
        passwd_layout.addWidget(passwd_text_2, 1, 1, 3, 1)
        passwd_layout.addWidget(passwd_text_3, 1, 2, 3, 1)

        passwd_1.setFixedSize(120, 30)
        passwd_2.setFixedSize(120, 30)
        passwd_3.setFixedSize(120, 30)
        passwd_widget.setStyleSheet(
            """
            QPushButton{
                border:none;
                color: black;
                border-left:4px solid black;
                text-align: left;
            }
            """
        )

        main_layout.addWidget(passwd_widget)

        bottom_widget = QtWidgets.QWidget()
        bottom_layout = QtWidgets.QGridLayout()
        bottom_widget.setLayout(bottom_layout)

        bottom_pushbutton_1 = QtWidgets.QPushButton("加密")
        bottom_pushbutton_2 = QtWidgets.QPushButton("解密")
        bottom_pushbutton_3 = QtWidgets.QPushButton("清空")
        bottom_layout.addWidget(bottom_pushbutton_1, 0, 0, 1, 1)
        bottom_layout.addWidget(bottom_pushbutton_2, 0, 1, 1, 1)
        bottom_layout.addWidget(bottom_pushbutton_3, 0, 2, 1, 1)
        bottom_pushbutton_1.setStyleSheet("""
        QPushButton{border:none;
        background:#199458;
        color:white;}
        QPushButton:pressed{font-weight:bold;}""")
        bottom_pushbutton_2.setStyleSheet("""QPushButton{border:none;
        background:#d1b468;
        color:white;}
        QPushButton:pressed{font-weight:bold;}""")
        bottom_pushbutton_3.setStyleSheet("""QPushButton{border:none;
        background:#b64f4c;
        color:white;}
        QPushButton:pressed{font-weight:bold;}""")
        bottom_pushbutton_1.setFixedSize(120, 50)
        bottom_pushbutton_2.setFixedSize(120, 50)
        bottom_pushbutton_3.setFixedSize(120, 50)

        main_layout.addWidget(bottom_widget)

        self.setTabText(1, "数据加密")
        self.tab2.setLayout(main_layout)

    def tab3UI(self):
        main_widget = QtWidgets.QWidget()
        main_layout = QtWidgets.QGridLayout()
        main_widget.setLayout(main_layout)

        left_widget = QWidget()
        left_layout = QGridLayout()
        left_widget.setLayout(left_layout)

        left_button_1 = QLabel("密钥协商")
        left_button_2 = QPushButton("公私钥生成")
        left_button_3 = QPushButton("密钥交换")
        left_button_1.setFixedSize(150, 40)
        left_button_1.setAlignment(QtCore.Qt.AlignCenter)
        left_button_1.setStyleSheet(
            """
                border:none;
                border-bottom: 4px solid black;
                font-size: 28px;
            """
        )

        left_layout.addWidget(left_button_1, 0, 0, 1, 1)
        left_layout.addWidget(left_button_2, 1, 0, 2, 1)
        left_layout.addWidget(left_button_3, 3, 0, 2, 1)
        left_button_2.setFixedSize(150, 60)
        left_button_3.setFixedSize(150, 60)
        left_widget.setStyleSheet(
            """
            QPushButton{
                color: white;
                background: #0b1012;
                border-radius: 10px;
                border: none;
            }
            QPushButton:pressed{
                background: #8f5b11;
                font-weight: bold;
            }
            """
        )

        main_layout.addWidget(left_widget, 0, 0, 1, 1)

        right_widget = QWidget()
        right_layout = QGridLayout()
        right_widget.setLayout(right_layout)

        right_pushbutton = QPushButton(qtawesome.icon('ei.tags', color='black'), "共享密钥")
        right_pushbutton.setIconSize(QtCore.QSize(35, 35))
        right_pushbutton.setStyleSheet(
            """
                border: none;
                border-bottom: 4px solid black;
                text-align: center;
                font-size: 24px;
            """
        )
        right_text = QTextEdit()

        right_layout.addWidget(right_pushbutton, 0, 0, 1, 1)
        right_layout.addWidget(right_text, 1, 0, 3, 1)

        main_layout.addWidget(right_widget, 0, 1, 1, 1)

        self.setTabText(2, "密钥协商")
        self.tab3.setLayout(main_layout)

    def tab4UI(self):
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

        label_1 = QLabel("发送区")
        label_1.setFixedSize(75, 40)
        label_1.setStyleSheet(
            """
            border:none;
            border-bottom: 3px solid black;
            font-weight:700;
            background: transparent; 
            border-radius:0px;
            font-size:20px;
            padding:2px 4px;
            """
        )
        label_1.setAlignment(QtCore.Qt.AlignCenter)
        left_layout.addWidget(label_1, 0, 0, 1, 1)
        left_layout.addWidget(QTextEdit(), 1, 0, 3, 1)

        label_2 = QLabel("接收区")
        label_2.setStyleSheet(
            """
            border:none;
            border-bottom: 3px solid black;
            font-weight:700;
            background: transparent; 
            border-radius:0px;
            font-size:20px;
            padding:2px 4px;
            """
        )
        label_2.setAlignment(QtCore.Qt.AlignCenter)
        label_2.setFixedSize(75, 40)
        right_layout.addWidget(label_2, 0, 0, 1, 1)
        right_layout.addWidget(QTextEdit(), 1, 0, 3, 1)


        bottom_buttom_1 = QPushButton("数字签名")
        bottom_buttom_1.setFixedSize(180, 60)
        bottom_buttom_2 = QPushButton("发送消息")
        bottom_buttom_2.setFixedSize(180, 60)
        bottom_layout.addWidget(bottom_buttom_1, 0, 0, 1, 1)
        bottom_layout.addWidget(bottom_buttom_2, 0, 1, 1, 1)

        bottom_widget.setStyleSheet(
            """
            QPushButton{
                color: white;
                background: #0b1012;
                border-radius: 10px;
                border: none;
            }
            QPushButton:pressed{
                background: #8f5b11;
                font-weight: bold;
            }
            """
        )

        main_layout.addWidget(left_widget, 0, 0, 3, 1)
        main_layout.addWidget(right_widget, 0, 1, 3, 1)
        main_layout.addWidget(bottom_widget, 3, 0, 1, 2)
        self.setTabText(3, "网络通信(AES)")
        self.tab4.setLayout(main_layout)

    def tab5UI(self):
        layout = QHBoxLayout()
        layout.addWidget(QTextEdit())
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
                font-family: "华文中宋";
                text-align: center;
            }
            """
        )
        self.tab2.setStyleSheet(
            """
                color:#black;
                font-size:20px;
                font-weight:100;
                padding-top: 2px;
                padding-bottom: 2px;
                padding-left: 2px;
                padding-right: 2px;
                font-family: "华文中宋";
            """
        )
        self.tab3.setStyleSheet(
            """
                color:#black;
                font-size:20px;
                font-weight:100;
                padding-top: 2px;
                padding-bottom: 2px;
                padding-left: 2px;
                padding-right: 2px;
                font-family: "华文中宋";

            """
        )
        self.tab4.setStyleSheet(
            """
                color:#black;
                font-size:20px;
                font-weight:100;
                padding-top: 2px;
                padding-bottom: 2px;
                padding-left: 2px;
                padding-right: 2px;
                font-family: "华文中宋";

            """
        )
        self.tab5.setStyleSheet(
            """
                color:#black;
                font-size:20px;
                font-weight:100;
                padding-top: 2px;
                padding-bottom: 2px;
                padding-left: 2px;
                padding-right: 2px;
                font-family: "华文中宋";

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