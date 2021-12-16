#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/16 1:19
# @Author  : Yiu
# @Site    : 
# @File    : login.py
# @Software: PyCharm
"""login,py"""
import qtawesome

"""登入界面"""
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton, QStackedLayout, QFormLayout
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPainter, QPainterPath
from PyQt5.QtWidgets import QLabel, QWidget, QHBoxLayout


class main_ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(main_ui, self).__init__()
        # 头衔布局
        self.pic_widget = QtWidgets.QWidget()
        self.pic_layout = QtWidgets.QGridLayout()
        self.pic_widget.setLayout(self.pic_layout)
        # 窗口选项
        self.left_close = QtWidgets.QPushButton("")
        self.left_visit = QtWidgets.QPushButton("")
        self.left_mini = QtWidgets.QPushButton("")
        self.left_widget = QtWidgets.QWidget()
        self.left_layout = QtWidgets.QHBoxLayout()
        self.left_widget.setLayout(self.left_layout)
        self.left_layout.addWidget(self.left_mini)
        self.left_layout.addWidget(self.left_close)
        self.left_layout.addWidget(self.left_visit)

        self.right_widget = QtWidgets.QWidget()
        self.head_widget = QtWidgets.QWidget()
        self.head_layout = QtWidgets.QGridLayout()
        self.head_widget.setLayout(self.head_layout)
        self.head_layout.addWidget(self.left_widget, 0, 0, 1, 2)
        self.head_layout.addWidget(self.right_widget, 0, 2, 1, 10)
        # 输入内容布局
        self.login_widget = QtWidgets.QWidget()
        self.login_layout = QtWidgets.QGridLayout()
        self.login_widget.setLayout(self.login_layout)
        # 主窗口
        self.main_widget = QtWidgets.QWidget()
        self.main_layout = QtWidgets.QGridLayout()
        self.main_widget.setLayout(self.main_layout)

        # 头像部件
        self.picture = QtWidgets.QLabel()
        # 登录部件
        self.user_name = QtWidgets.QPushButton("邮箱")
        self.email_edit = QtWidgets.QLineEdit()
        self.email_edit.setPlaceholderText('Please enter your valid email.')
        self.email_suffix = QtWidgets.QComboBox()
        self.email_suffix.addItems(['@gmail.com', '@qq.com', '@163.com'])

        # formLayout = QFormLayout()
        self.password = QtWidgets.QPushButton("密码")
        self.passwd_edit = QtWidgets.QLineEdit()
        # formLayout.addRow("Password", self.passwd_edit)
        # self.passwd_edit.setPlaceholderText("Password")
        self.passwd_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwd_edit.setPlaceholderText('Enter your password.')
        self.passwd_login = QtWidgets.QPushButton(qtawesome.icon('fa.arrow-circle-right', color='white'), "")
        self.passwd_login.setIconSize(QtCore.QSize(40, 40))
        self.init_ui()
        self.setWindowOpacity(0.9)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # self.main_layout.setSpacing(0)
        # self.login_layout.setSpacing(0)
    """初始界面"""
    def init_ui(self):
        # 登入界面的大小
        self.setFixedSize(550, 580)
        # 登录头像
        self.head_icon()
        # 界面修饰
        self.decorate()
        # 将部件嵌入
        self.main_layout.addWidget(self.head_widget, 0, 0, 1, 1)
        self.pic_layout.addWidget(self.picture)
        self.main_layout.addWidget(self.pic_widget, 1, 0, 10, 1)
        self.main_layout.addWidget(self.login_widget, 11, 0, 6, 1)

        self.login_layout.addWidget(self.user_name, 0, 0, 1, 1)
        self.login_layout.addWidget(self.email_edit, 0, 1, 1, 1)
        self.login_layout.addWidget(self.email_suffix, 0, 2, 1, 1)
        self.login_layout.addWidget(self.password, 1, 0, 1, 1)
        self.login_layout.addWidget(self.passwd_edit, 1, 1, 1, 1)
        self.login_layout.addWidget(self.passwd_login, 1, 2, 1, 1)

        self.setCentralWidget(self.main_widget)
    """登录头像"""
    def head_icon(self):
        self.picture.setMaximumSize(200, 200)
        self.picture.setMinimumSize(200, 200)
        self.picture.radius = 100
        self.picture.target = QPixmap(self.picture.size())
        self.picture.target.fill(Qt.transparent)
        p = QPixmap("head.jpg")
        painter = QPainter(self.picture.target)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setRenderHint(QPainter.HighQualityAntialiasing, True)
        painter.setRenderHint(QPainter.SmoothPixmapTransform, True)
        path = QPainterPath()
        path.addRoundedRect(0, 0, self.picture.width(), self.picture.height(), self.picture.radius, self.picture.radius)
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, p)
        self.picture.setPixmap(self.picture.target)
    """QSS修饰"""
    def decorate(self):
        self.main_widget.setStyleSheet(
            """
            QWidget#main_widget{
                border-image:url(./head.jpg);
            }
            QWidget{
                color:#afb1b3;
                background: black;
                font-size:20px;
                font-weight:100;
                padding-top: 2px;
                padding-bottom: 2px;
                border: 1px solid white;
                border-radius: 10px;
                font-family: "Century Schoolbook";
            }

            """
        )
        self.user_name.setFixedSize(80, 40)
        self.user_name.setStyleSheet(
            """
                color: white;
                font-weight:500;
                border-radius: 10px;
                background:#90df8c;
            """
        )
        self.email_edit.setFixedSize(300, 40)
        self.email_edit.setStyleSheet(
            """
                border:1px solid gray;
                width:300px;
                border-radius:10px;
                padding:2px 4px;
            """
        )
        self.email_suffix.setFixedSize(115, 40)
        self.email_suffix.setStyleSheet(
            """
            QComboBox{
                font-size:16px;
                border: 1px solid gray;
                border-radius: 10px;
                outline:none;
                color: gray;
            }
            QComboBox:drop-down{
                border:none;
            }
            """
        )
        self.password.setFixedSize(80, 40)
        self.password.setStyleSheet(
            """
                QPushButton{
                    font-weight:500;
                    border-radius: 10px;
                    background:#fc526f;
                    color: #edffe4;
                }
            """
        )
        self.passwd_edit.setFixedSize(300, 40)
        self.passwd_edit.setStyleSheet(
            """
                border:1px solid gray;
                width:300px;
                border-radius:10px;
                padding:2px 4px;
            """
        )
        self.passwd_login.setFixedSize(40, 40)
        self.passwd_login.setStyleSheet(
            """
                QPushButton{
                    background:#2f7bc6;
                    border-radius:10px;
                }
                QPushButton:pressed{
                    background:green;
                    border-radius:20px;
                }
            """
        )
        self.left_close.setFixedSize(15, 15)
        self.left_visit.setFixedSize(15, 15)
        self.left_mini.setFixedSize(15, 15)
        self.left_close.setStyleSheet('''QPushButton{
        background:#F76677;
        border-radius:5px;}
        QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet('''QPushButton{
        background:#F7D674;
        border-radius:5px;}
        QPushButton:hover{background:red;}''')
        self.left_mini.setStyleSheet('''QPushButton{
        background:#6DDF6D;
        border-radius:5px;}
        QPushButton:hover{background:red;}''')
        self.picture.setStyleSheet(
            """
            border: none;
            """
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = main_ui()
    win.show()
    sys.exit(app.exec_())
from qtawesome import icon_browser
icon_browser.run()
