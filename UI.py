#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/11 19:46
# @Author  : Yiu
# @Site    :
# @File    : UI.py
# @Software: PyCharm
"""
图形化界面设计
"""
from PyQt5.QtGui import QMouseEvent

"""
常用模块：
- QtCore: 包含非GUI的功能设计，这个模块用来实现时间，文件和目录，不同数据类型，流，URL，mime类型，线程和进行
- QtGui：模块包含的类用于窗口化的系统结构，事件处理，2D绘图，基本图形，字体和文本
- QtWidgets：模块包含的类提供了一套UI元素来创建经典桌面风格用户界面
- QtMultimedia：模块包含的类用于处理多媒体内容和链接摄像头和无线电功能的API
- QtBluetooth：模块包含的类用于扫描蓝牙设备，并且和他们建立连接互动
- QtNetwork：模块包含的类用于网络编程，这些类使TCP/IP和UDP客户端/服务端编程更加容易和轻便
- QtPositioning：模块包含的类用于多种可获得资源的位置限定，包含卫星定位，Wi-Fi，或一个文本文件
- Enginio：模块用于解决客户端访问Qt云服务托管
- QtWebSockets：模块用于解决客户端访问Qt云服务托管
- QtWebKit：包含的关于浏览器的类用于解决基于WebKit2的支持库
- QtWebKitWidgets：模块包含的关于WebKit1的类基本解决浏览器使用基于QtWidgets应用问题
- QtXml：QtXml 模块包含的类用于解析XML文件
- QtSvg：模块提供类用于显示SVG文件内容
- QtSql：模块提供类驱动数据库工作
- QtTest：模块包含了方法提供PyQt5应用的单元测试
"""

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import qtawesome
from tapUI import TabDemo
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication
from selenium import webdriver
import time


class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainUi, self).__init__()
        # 创建窗口组部件
        self.main_widget = QtWidgets.QWidget()
        # 创建主部件的网络布局
        self.main_layout = QtWidgets.QGridLayout()
        # 设置窗口主部件的布局为网络布局
        self.main_widget.setLayout(self.main_layout)

        self.init_ui()
        self.connect()

    def click_even(self):
        self.right_widget.show()

    def click_even_2(self):
        self.right_widget.hide()

    def init_left(self):
        # 创建左部件
        self.left_widget = QtWidgets.QWidget()
        # 设置对象的名字
        self.left_widget.setObjectName('left_widget')
        # 创建左侧部件的网络布局层
        self.left_layout = QtWidgets.QGridLayout()
        # 设置左部件布局为网络布局
        self.left_widget.setLayout(self.left_layout)

        # 左半部分的UI设计
        self.left_close = QtWidgets.QPushButton("")
        self.left_close.setToolTip("关闭")
        self.left_visit = QtWidgets.QPushButton("")
        self.left_mini = QtWidgets.QPushButton("")
        self.left_mini.setToolTip("最小化")

        self.left_close.clicked.connect(QCoreApplication.instance().quit)
        self.left_mini.clicked.connect(self.showMinimized)

        self.left_label_1 = QtWidgets.QPushButton("密码学知识")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("学习内容")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("联系与帮助")
        self.left_label_3.setObjectName('left_label')
        self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('ei.fire', color='white'), "趣闻轶事")
        self.left_button_1.setObjectName('left_button')
        self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('ei.rss', color='white'), "经典算法")
        self.left_button_2.setObjectName('left_button')
        self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.diamond', color='white'), "相关文献")
        self.left_button_3.setObjectName('left_button')
        self.left_button_4 = QtWidgets.QPushButton(qtawesome.icon('fa.send', color='white'), "开发记录")
        self.left_button_4.setObjectName('left_button')
        self.left_button_5 = QtWidgets.QPushButton(qtawesome.icon('fa.gitlab', color='white'), "引用博客")
        self.left_button_5.setObjectName('left_button')
        self.left_button_6 = QtWidgets.QPushButton(qtawesome.icon('fa.firefox', color='white'), "推荐文章")
        self.left_button_6.setObjectName('left_button')
        self.left_button_7 = QtWidgets.QPushButton(qtawesome.icon('fa5b.github', color='white'), "项目仓库")
        self.left_button_7.setObjectName('left_button')
        self.left_button_8 = QtWidgets.QPushButton(qtawesome.icon('ei.envelope', color='white'), "关注我们")
        self.left_button_8.setObjectName('left_button')
        self.left_button_9 = QtWidgets.QPushButton(qtawesome.icon('fa5.comment-dots', color='white'), "遇到问题")
        self.left_button_9.setObjectName('left_button')

        self.left_button_1.clicked.connect(self.p1_event)
        self.left_button_2.clicked.connect(self.p2_event)
        self.left_button_3.clicked.connect(self.p3_event)
        self.left_button_4.clicked.connect(self.p4_event)
        self.left_button_5.clicked.connect(self.p5_event)
        self.left_button_6.clicked.connect(self.p6_event)
        self.left_button_7.clicked.connect(self.p7_event)
        self.left_button_8.clicked.connect(self.p8_event)
        self.left_button_9.clicked.connect(self.p9_event)

        self.left_button_1.setIconSize(QtCore.QSize(20, 20))
        self.left_button_2.setIconSize(QtCore.QSize(20, 20))
        self.left_button_3.setIconSize(QtCore.QSize(20, 20))
        self.left_button_4.setIconSize(QtCore.QSize(20, 20))
        self.left_button_5.setIconSize(QtCore.QSize(20, 20))
        self.left_button_6.setIconSize(QtCore.QSize(20, 20))
        self.left_button_7.setIconSize(QtCore.QSize(20, 20))
        self.left_button_8.setIconSize(QtCore.QSize(20, 20))
        self.left_button_9.setIconSize(QtCore.QSize(20, 20))

        self.left_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)

        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_1, 2, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_2, 3, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_3, 4, 0, 1, 3)

        self.left_layout.addWidget(self.left_label_2, 5, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_4, 6, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_5, 7, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_6, 8, 0, 1, 3)

        self.left_layout.addWidget(self.left_label_3, 9, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_7, 10, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_8, 11, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_9, 12, 0, 1, 3)

    def init_right(self):
        # 创建右部件
        self.right_widget = QtWidgets.QWidget()
        # 设置对象的名字
        self.right_widget.setObjectName('right_widget')
        # 创建右部件的网络布局层
        self.right_layout = QtWidgets.QGridLayout()
        # 设置右部件布局为网络布局
        self.right_widget.setLayout(self.right_layout)

        self.info_bar()
        self.search_bar()
        self.exp_bar()

    def info_bar(self):
        self.right_info_widget = QtWidgets.QWidget()
        self.right_info_layout = QtWidgets.QGridLayout()
        self.right_info_widget.setLayout(self.right_info_layout)

        self.left_info_head = QtWidgets.QTextBrowser()
        # self.left_info_head.setFixedSize(850, 100)
        self.left_info_label = QLabel("操作信息")
        self.left_info_label.setStyleSheet(
            """
                font-family:"华文中宋";
                font-size: 24px;
            """
        )
        self.left_info_head.setStyleSheet(
            """
                font-family:"华文中宋";
                font-size: 16px;
            """
        )

        self.right_info_head = QtWidgets.QToolButton()
        self.right_info_head.setIcon(QtGui.QIcon('./head.jpg'))
        self.right_info_head.setIconSize(QtCore.QSize(30, 30))

        self.display_name = QtWidgets.QLabel("Yiu")
        self.display_name.setAlignment(QtCore.Qt.AlignCenter)

        self.color_setting = QtWidgets.QPushButton(qtawesome.icon('ri.user-settings-fill', color='black'), "")
        self.color_setting.setIconSize(QtCore.QSize(30, 30))
        self.sys_setting = QtWidgets.QPushButton(qtawesome.icon('ri.settings-4-fill', color='black'), "")
        self.sys_setting.setIconSize(QtCore.QSize(30, 30))

        self.right_info_layout.addWidget(self.left_info_label, 0, 0, 1, 3)
        self.right_info_layout.addWidget(self.left_info_head, 1, 0, 1, 3)
        # self.right_info_layout.addWidget(self.right_info_head, 0, 3, 1, 1)
        # self.right_info_layout.addWidget(self.display_name, 0, 4, 1, 1)
        # self.right_info_layout.addWidget(self.color_setting, 0, 5, 1, 1)
        # self.right_info_layout.addWidget(self.sys_setting, 0, 6, 1, 1)
        self.right_layout.addWidget(self.right_info_widget, 16, 0, 1, 9)

    def search_bar(self):
        # 右侧顶部搜索部件
        self.right_bar_widget = QtWidgets.QWidget()
        # 右侧顶部搜索网络布局
        self.right_bar_layout = QtWidgets.QGridLayout()
        self.right_bar_widget.setLayout(self.right_bar_layout)
        self.search_icon = QtWidgets.QPushButton(qtawesome.icon('mdi.find-replace', color='black'), "搜索")
        self.search_icon.setIconSize(QtCore.QSize(40, 40))
        self.right_bar_widget_search_input = QtWidgets.QLineEdit()
        self.right_bar_widget_search_input.setPlaceholderText('输入内容，回车进行搜索')
        self.right_bar_layout.addWidget(self.search_icon, 0, 0, 1, 1)

        self.right_bar_layout.addWidget(self.right_bar_widget_search_input, 0, 1, 1, 8)
        self.right_layout.addWidget(self.right_bar_widget, 0, 0, 1, 9)

        self.right_bar_widget_search_input.returnPressed.connect(self.search_by_baidu)

    def search_by_baidu(self):
        chrome_driver = r"./chromedriver.exe"
        driver = webdriver.Chrome(executable_path=chrome_driver)
        url = 'https://www.baidu.com/'
        # 访问
        driver.get(url)
        # 最大化窗口
        driver.maximize_window()
        time.sleep(1)
        # 找到输入框
        shuru = driver.find_element_by_id('kw')
        # 在输入框中放搜索内容

        shuru.send_keys(self.right_bar_widget_search_input.text())
        time.sleep(1)

        # 找到百度一下按钮
        sousuo = driver.find_element_by_id('su')
        # 点击某个对象（点击百度一下）
        sousuo.click()
        time.sleep(10)

    def p1_event(self):
        chrome_driver = r"./chromedriver.exe"
        driver = webdriver.Chrome(executable_path=chrome_driver)
        url = 'https://www.zhihu.com/question/31871888/answer/1301925317'
        # 访问
        driver.get(url)
        # 最大化窗口
        driver.maximize_window()
        time.sleep(10)

    def p2_event(self):
        chrome_driver = r"./chromedriver.exe"
        driver = webdriver.Chrome(executable_path=chrome_driver)
        url = 'https://www.cnblogs.com/tianxia2s/p/8735079.html'
        # 访问
        driver.get(url)
        # 最大化窗口
        driver.maximize_window()
        time.sleep(10)

    def p3_event(self):
        chrome_driver = r"./chromedriver.exe"
        driver = webdriver.Chrome(executable_path=chrome_driver)
        url = 'https://zhuanlan.zhihu.com/p/52208681'
        # 访问
        driver.get(url)
        # 最大化窗口
        driver.maximize_window()
        time.sleep(10)

    def p4_event(self):
        chrome_driver = r"./chromedriver.exe"
        driver = webdriver.Chrome(executable_path=chrome_driver)
        url = r'https://github.com/Dominique-Yiu/cryptology_exp/blob/master/README.md'
        # 访问
        driver.get(url)
        # 最大化窗口
        driver.maximize_window()
        time.sleep(10)

    def p5_event(self):
        chrome_driver = r"./chromedriver.exe"
        driver = webdriver.Chrome(executable_path=chrome_driver)
        url = 'https://github.com/Dominique-Yiu/cryptology_exp/blob/master/README.md'
        # 访问
        driver.get(url)
        # 最大化窗口
        driver.maximize_window()
        time.sleep(10)

    def p6_event(self):
        chrome_driver = r"./chromedriver.exe"
        driver = webdriver.Chrome(executable_path=chrome_driver)
        url = 'https://github.com/Dominique-Yiu/cryptology_exp/blob/master/README.md'
        # 访问
        driver.get(url)
        # 最大化窗口
        driver.maximize_window()
        time.sleep(10)

    def p7_event(self):
        chrome_driver = r"./chromedriver.exe"
        driver = webdriver.Chrome(executable_path=chrome_driver)
        url = 'https://github.com/Dominique-Yiu/cryptology_exp'
        # 访问
        driver.get(url)
        # 最大化窗口
        driver.maximize_window()
        time.sleep(10)

    def p8_event(self):
        chrome_driver = r"./chromedriver.exe"
        driver = webdriver.Chrome(executable_path=chrome_driver)
        url = 'https://www.hnu.edu.cn/'
        # 访问
        driver.get(url)
        # 最大化窗口
        driver.maximize_window()
        time.sleep(10)

    def p9_event(self):
        chrome_driver = r"./chromedriver.exe"
        driver = webdriver.Chrome(executable_path=chrome_driver)
        url = 'https://stackoverflow.com/'
        # 访问
        driver.get(url)
        # 最大化窗口
        driver.maximize_window()
        time.sleep(10)

    def exp_bar(self):
        self.tab = TabDemo()
        self.right_layout.addWidget(self.tab, 1, 0, 15, 9)

    def init_ui(self):
        self.setFixedSize(1200, 900)

        self.init_left()
        self.init_right()

        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)
        # 右侧部件在第0行第3列，占8行9列
        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)
        self.setCentralWidget(self.main_widget)

        self.decorate()
        self.left_visit.released.connect(self.click_even)
        self.left_visit.pressed.connect(self.click_even_2)

        self.setWindowIcon(QtGui.QIcon(qtawesome.icon('mdi.steam', color='white')))

        self.setWindowIcon(QtGui.QIcon(qtawesome.icon('mdi.steam', color='white')))

    def decorate(self):
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
        self.left_widget.setStyleSheet(
            '''
                QPushButton{border:none;color:white;font-size:16px;font-family:"华文中宋";}
                QPushButton#left_label{
                    border:none;
                    border-bottom:1px solid white;
                    font-size:22px;
                    font-weight:700;
                    font-family:"华文中宋";
                }
                QWidget#left_widget{
                    background: black;
                    border-top: 1px solid white;
                    border-bottom: 1px solid white;
                    border-left: 1px solid white;
                    border-top-left-radius: 10px;
                    border-bottom-left-radius: 10px;
                }
                QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
            '''
        )
        self.search_icon.setStyleSheet(
            """
            QPushButton{
                    font-family:"华文中宋";
                    font-size: 16px;
                    border:none;
            }
            """
        )
        self.right_bar_widget_search_input.setStyleSheet(
            '''
                QLineEdit{
                        border:1px solid gray;
                        width:300px;
                        height: 30px;
                        border-radius:10px;
                        padding:2px 4px;
                        font-size: 16px;
                        font-family:"华文中宋";
                }'''
        )
        self.right_widget.setStyleSheet(
            '''
            QWidget#right_widget{
                color:#232C51;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
            }
            QLabel#right_lable{
                border:none;
                font-size:16px;
                font-weight:700;
                font-family:"华文中宋";
            }
        '''
        )
        self.color_setting.setFixedSize(100, 30)
        self.sys_setting.setFixedSize(100, 30)
        self.display_name.setFixedSize(100, 30)
        self.right_info_widget.setStyleSheet(
            """
            QPushButton{
                border:none;
                border-radius: 10px;
            }
            QPushButton:pressed{
                background: gray;
            }
            QToolButton{
                border:1px solid gray;
            }
            """
        )
        self.display_name.setStyleSheet(
            """
                border:none;
                font-weight:500;
                font-family:"华文中宋";
            """
        )

        self.setWindowOpacity(0.9)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.main_layout.setSpacing(0)

    def connect(self):
        # 连接网络按钮
        self.tab.tap1_bottom_buttom_1.clicked.connect(self.click_On_net)
        # 断开网络按钮
        self.tab.tap1_bottom_buttom_2.clicked.connect(self.click_Off_net)
        # 公私钥生成
        self.tab.tap3_left_button_2.clicked.connect(self.click_PP_key)
        # 密钥交换
        self.tab.tap3_left_button_3.clicked.connect(self.click_Change_key)
        # 数字签名
        self.tab.tap4_bottom_buttom_1.clicked.connect(self.click_RSA_sign)
        # 发送消息
        self.tab.tap4_bottom_buttom_2.clicked.connect(self.click_Send_msg)
        # 清空 1
        self.tab.clear_1.clicked.connect(self.click_Plain_clear)
        # 清空 2
        self.tab.clear_2.clicked.connect(self.click_Cipher_clear)
        # 清空 3
        self.tab.clear_3.clicked.connect(self.click_Setting_clear)
        # 清空 4
        self.tab.tap2_bottom_pushbutton_3.clicked.connect(self.click_All_clear)
        # 加密
        self.tab.tap2_bottom_pushbutton_1.clicked.connect(self.click_Encrypt)
        # 解密
        self.tab.tap2_bottom_pushbutton_2.clicked.connect(self.click_Decrypt)
        # 清除服务端
        self.tab.tab5Button_1.clicked.connect(self.remove_serverText)
        # 清除客户端
        self.tab.tab5Button_3.clicked.connect(self.remove_ClientText)
        # 发送给客户端
        self.tab.tab5Button_2.clicked.connect(self.ssl_server_send)
        # 发送给服务端
        self.tab.tab5Button_4.clicked.connect(self.ssl_client_send)
        # 启动服务端
        self.tab.tab5Button_5.clicked.connect(self.ssl_start_server)
        # 启动客户端
        self.tab.tab5Button_6.clicked.connect(self.ssl_start_client)
        # 关闭进程
        self.tab.tab5_Stop.clicked.connect(self.ssl_end_threading)

    def ssl_end_threading(self):
        raise NotImplementedError

    def ssl_start_server(self):
        raise NotImplementedError

    def ssl_start_client(self):
        raise NotImplementedError

    def remove_serverText(self):
        raise NotImplementedError

    def remove_ClientText(self):
        raise NotImplementedError

    def ssl_server_send(self):
        raise NotImplementedError

    def ssl_client_send(self):
        raise NotImplementedError

    def click_On_net(self):
        raise NotImplementedError

    def click_Off_net(self):
        raise NotImplementedError

    def click_PP_key(self):
        raise NotImplementedError

    def click_Change_key(self):
        raise NotImplementedError

    def click_RSA_sign(self):
        raise NotImplementedError

    def click_Send_msg(self):
        raise NotImplementedError

    def click_Plain_clear(self):
        raise NotImplementedError

    def click_Cipher_clear(self):
        raise NotImplementedError

    def click_Setting_clear(self):
        raise NotImplementedError

    def click_All_clear(self):
        raise NotImplementedError

    def click_Encrypt(self):
        raise NotImplementedError

    def click_Decrypt(self):
        raise NotImplementedError

    def send_Show_msg(self, msg):
        self.left_info_head.append(msg)
        self.left_info_head.moveCursor(QtGui.QTextCursor.End)


def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
