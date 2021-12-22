#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/22 16:40
# @Author  : Yiu
# @Site    : 
# @File    : main.py
# @Software: PyCharm
import base64
import threading

from PyQt5 import *
from PyQt5.QtWidgets import *
import UI
import socket
import os
import sys
import binascii
import datetime
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import MD5


class udp_logic(UI.MainUi):
    def __init__(self):
        super(udp_logic, self).__init__()
        self.udp_clientsocket = None
        self.udp_serversocket = None
        self.recv_pk = None
        self.public_key = None
        self.private_key = None
        self.sendaddress = None
        self.recvaddress = None
        self.link = False
        self.rand_a = None
        self.recv_rand_a = None
        self.share_key = None
        self.send_msg = None

    # 实现连接网络的控件，生产子线程监听端口
    def click_On_net(self):
        # 作为发送方（客户端）的网络设置
        self.udp_clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            self.sendaddress = (str(self.Recv_ip.text()), int(self.Recv_port.text()))
        except Exception as e:
            msg = '发送端设置异常,请检查目标IP，目标端口\n'
            self.send_Show_msg(msg)
        else:
            self.link = True
            msg = '发送端已启动\n'
            self.send_Show_msg(msg)
        # 作为接收方(服务器)的网络设置
        self.udp_serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            self.recvaddress = (str(self.Send_ip.text()), int(self.Send_port.text()))
            self.udp_serversocket.bind(self.recvaddress)
            # 启动接收线程

        except Exception as e:
            msg = '接收端设置异常，请检查目标端口\n'
            self.send_Show_msg(msg)
        else:
            self.recv_thread = threading.Thread(target=self.server_recv)
            self.recv_thread.start()
            self.link = True
            msg = '接收端端正在监听端口:{}\n'.format(int(self.Send_port.text()))
            self.send_Show_msg(msg)
