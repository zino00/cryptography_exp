import base64
import threading

from PyQt5 import QtWidgets
import socket
import sys
import binascii
import crypto
import _dh
import datetime
import UI
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import MD5
import ssl
import pprint

class udp_logic(UI.MainUi):
    def __init__(self):
        # 调用父类的init函数
        super(udp_logic, self).__init__()
        self.udp_clientsocket = None
        self.udp_serversocket = None
        self.recv_pk = None
        self.public_key = None
        self.private_key = None
        self.sendaddress = None
        self.recvaddress = None
        self.link = False
        self.XA = None
        self.XB = None
        self.recv_YA = None
        self.recv_YB = None
        self.share_key = None
        self.send_msg = None

        self.ssl_client_socket = None
        self.ssl_server_socket = None
        self.ssl_connect_sock = None
        self.ssl_address = None
        self.ssl_server_thread = None
        self.ssl_client_thread = None

    # 实现连接网络的控件，生产子线程监听端口
    def click_On_net(self):
        # 作为发送方（客户端）的网络设置
        self.send_Show_msg((str(self.tab.tap1_read_line.text())))
        self.udp_clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            self.sendaddress = (str(self.tab.tap1_read_line.text()), int(self.tab.tap1_read_line_1.text()))
        except Exception:
            msg = '发送端设置异常,请检查目标IP，目标端口\n'
            self.send_Show_msg(msg)
        else:
            self.link = True
            msg = '发送端已启动\n'
            self.send_Show_msg(msg)
        # 作为接收方(服务器)的网络设置
        self.udp_serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            self.recvaddress = (str(self.tab.tap1_read_line_2.text()), int(self.tab.tap1_read_line_3.text()))
            self.udp_serversocket.bind(self.recvaddress)
            # 启动接收线程

        except Exception:
            msg = '接收端设置异常，请检查目标端口\n'
            self.send_Show_msg(msg)
        else:
            self.recv_thread = threading.Thread(target=self.server_recv)
            self.recv_thread.start()
            self.link = True
            msg = '接收端端正在监听端口:{}\n'.format(int(self.tab.tap1_read_line_3.text()))
            self.send_Show_msg(msg)

    # 实现断开网络控件
    def click_Off_net(self):
        try:
            self.udp_serversocket.close()
            self.udp_clientsocket.close()
            if self.link is True:
                msg = '已断开网络\n'
                self.send_Show_msg(msg)
        except Exception as ret:
            msg = '网络尚未连接\n'
            self.send_Show_msg(msg)
            pass

    # 实现接受线程的功能函数
    def server_recv(self):
        while True:
            try:
                # 接收发送过来的字符
                recv_msg, recv_addr = self.udp_serversocket.recvfrom(1024)
                if recv_msg[:4] == b'[#5]':  # 接收到签名的消息验证后显示
                    recv_msg = recv_msg[4:]
                    msg = '来自IP:{} 端口: {} 的消息:'.format(recv_addr[0], recv_addr[1])
                    self.send_Show_msg(msg)

                    aes = crypto.aes_crypto(str(self.share_key)[:16].encode())
                    print(recv_msg)
                    # self.tab.tap4_textedit_2.appendPlainText(str(recv_msg))
                    s1 = aes.decrypt(recv_msg).decode()  # 原消息aes解密
                    msg = '消息解密成功,开始验证消息签名\n'
                    self.send_Show_msg(msg)
                    # 签名验证
                    message = s1.split('||')[0]  # 原消息
                    signer = s1.split('||')[1]  # 消息签名
                    bytes = base64.b64decode(signer.encode())
                    h = MD5.new(message.encode())
                    verifier = PKCS1_v1_5.new(self.public_key)
                    if verifier.verify(h, bytes):
                        msg = '签名验证成功\n'
                        self.send_Show_msg(msg)
                    else:
                        msg = '无效签名\n'
                        self.send_Show_msg(msg)
                    self.tab.tap4_textedit_2.appendPlainText(message)
                    msg = '已成功输出经过签名验证的明文!\n'
                    self.send_Show_msg(msg)
                    continue
                recv_msg = recv_msg.decode()
                # 将bytes类型的数据用utf-8进行编码
                msg = '来自IP:{} 端口: {} 的消息:' .format(recv_addr[0], recv_addr[1])
                if recv_msg[:4] == '[#1]':  # 接受公钥
                    self.send_Show_msg(msg)
                    self.recv_pk = recv_msg[4:].encode()
                    msg = '接受公钥成功'
                    self.send_Show_msg(msg+'\n'+self.recv_pk.decode()+'\n')
                if recv_msg[:4] == '[#2]':  # 协商共享密钥
                    test = _dh.ex_DH(self.private_key, self.public_key)
                    self.XB = test.random_key()
                    YB = test.get_calculation(self.XB)
                    #sign = test.rsa_sign(str(YB))
                    self.client_send('[#4]', '[#4]' + str(YB))
                    self.send_Show_msg(msg)
                    recv_key = recv_msg[4:]  # 接收到的YA
                    self.recv_YA = _dh.atoi(recv_key)  # 字符转化为数字
                    self.share_key = test.get_key(self.XB, self.recv_YA)
                    msg = '对方DH协商安全参数' + str(recv_key)+'\n'
                    self.send_Show_msg(msg)
                    msg = '身份认证通过。共享密钥生成成功!\n'
                    self.send_Show_msg(msg)
                    msg = str(self.share_key)[:16]
                    self.tab.tap3_right_text.append(msg)
                if recv_msg[:4] == '[#3]':  # 认证签名
                    self.send_Show_msg(msg)
                    recv_sign = _dh.atoi(recv_msg[4:])
                    test = _dh.ex_DH(self.private_key, self.recv_pk)
                    flag = test.rsa_verify(str(self.recv_rand_a), recv_sign)
                    if flag == True:
                        msg = '签名认证通过\n'
                        self.send_Show_msg(msg)
                if recv_msg[:4] == '[#4]':  # 身份认证
                    test = _dh.ex_DH(self.private_key, self.public_key)
                    self.send_Show_msg(msg)
                    recv_key = recv_msg[4:]
                    self.recv_YB = _dh.atoi(recv_key)
                    self.share_key = test.get_key(self.XA, self.recv_YB)
                    msg = '对方DH协商安全参数' + str(recv_key)+'\n'
                    self.send_Show_msg(msg)
                    msg = '身份认证通过。共享密钥生成成功!\n'
                    self.send_Show_msg(msg)
                    msg = str(self.share_key)[:16]
                    self.tab.tap3_right_text.append(msg)
            except Exception as e:
                break

    # 用于通信的发送消息函数的具体实现
    def client_send(self, op, msg):
        # 发送用于rsa签名的公钥
        if op == '[#1]':
            self.udp_clientsocket.sendto(msg.encode(), self.sendaddress)
            self.send_Show_msg('成功发送公钥\n')
        if op == '[#2]':
            self.udp_clientsocket.sendto(msg.encode(), self.sendaddress)
            self.send_Show_msg('成功发送x^a%p\n')
        if op == '[#3]':
            self.udp_clientsocket.sendto(msg.encode(), self.sendaddress)
            self.send_Show_msg('签名成功\n')
        if op == '[#4]':
            self.udp_clientsocket.sendto(msg.encode(), self.sendaddress)
            self.send_Show_msg('成功发送x^a%p\n')

    # 生产公私钥，并且发送公钥
    def click_PP_key(self):
        test = _dh.Gen_Key()
        self.public_key = test.get_pub()
        self.private_key = test.get_pri()
        self.send_Show_msg(str(test.public_key)+'\n')
        self.send_Show_msg(str(test.private_key)+'\n')
        self.client_send('[#1]', '[#1]' + str(self.public_key))

    # DH协议协商共享密钥
    def click_Change_key(self):
        test = _dh.ex_DH(self.private_key, self.public_key)
        self.XA = test.random_key()
        YA = test.get_calculation(self.XA)
        sign = test.rsa_sign(str(YA))
        self.client_send('[#2]', '[#2]'+str(YA))

    # 同通信的消息用AES加密后，在使用RSA签名进行发送
    def click_RSA_sign(self):
        # test=_dh.ex_DH(self.private_key, self.public_key)
        message = self.tab.tap4_textedit_1.toPlainText()
        # 签名
        h = MD5.new(message.encode())
        rsa = PKCS1_v1_5.new(self.private_key)
        signature = rsa.sign(h)
        s2 = base64.b64encode(signature)
        # 加密消息本身和签名
        s1 = message.encode()
        s3 = s1+'||'.encode()+s2
        aes = crypto.aes_crypto(str(self.share_key)[:16].encode())  # 利用共享密钥进行aes加密
        self.send_msg = aes.encrypt(s3)  #加密
        self.tab.tap4_textedit_1.clear()
        self.tab.tap4_textedit_1.appendPlainText(str(self.send_msg))
        self.send_Show_msg('AES加密和数字签名完成!\n加密并签名后的消息如下：')
        self.send_Show_msg(str(self.send_msg))

    # 实现发送消息的控件
    def click_Send_msg(self):
        self.send_msg = '[#5]'.encode() + self.send_msg
        self.udp_clientsocket.sendto(self.send_msg, self.sendaddress)
        self.send_Show_msg('成功发送消息\n')

    # 加密控件的实现
    def click_Encrypt(self):
        key = self.tab.passwd_text_3.toPlainText()
        p = self.tab.passwd_text_1.toPlainText()
        if self.tab.pushbutton_1.text() == '仿射加密':
            test = crypto.Radiate()
            TextPlain = test.encryption(p.encode(), key.encode())
            self.send_Show_msg(TextPlain)
            self.tab.passwd_text_2.setPlainText(TextPlain)
            self.send_Show_msg(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '：仿射加密成功!')
        elif self.tab.pushbutton_1.text() == '流密码加密':
            if self.tab.comboBox.currentIndex() == 1:
                test = crypto.cypto_LFSR(key)
                TextPlain = test.do_crypt(p.encode())
                TextPlain = base64.b64encode(TextPlain)
                self.tab.passwd_text_2.setPlainText(TextPlain.decode())
                self.send_Show_msg(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '：LSFR+J-K加密成功!')
            elif self.tab.comboBox.currentIndex() == 0:
                test = crypto.RC4(key.encode())
                TextPlain = test.do_crypt(p.encode())
                self.tab.passwd_text_2.setPlainText(TextPlain.decode())
                self.send_Show_msg(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '：RC4加密成功!')
        elif self.tab.pushbutton_1.text() == '对称加密':
            if self.tab.comboBox.currentIndex() == 0:
                test = crypto.des_crypto(key.encode())
                TextCipher = test.encrypt(p.encode())
                self.tab.passwd_text_2.setPlainText(str(binascii.b2a_hex(TextCipher))[2:-1])
                self.send_Show_msg(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '：DES加密成功!')
            elif self.tab.comboBox.currentIndex() == 1:
                test = crypto.aes_crypto(key.encode())
                TextCipher = test.encrypt(p.encode())
                self.tab.passwd_text_2.setPlainText(str(binascii.b2a_hex(TextCipher))[2:-1])
                self.send_Show_msg(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '：AES加密成功!')
        elif self.tab.pushbutton_1.text() == '非对称加密':
            if self.tab.comboBox.currentIndex() == 0:
                test = crypto.RSA()
                TextCipher = test.Encrypt(p)
                msg = ''
                for i in TextCipher:
                    if i != 0:
                        msg += str(hex(i))[2:10] + ' '
                self.tab.passwd_text_2.setPlainText(msg)
                self.send_Show_msg(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '：RSA加密成功!')
        else:
            self.send_Show_msg(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '：请选择加密方式!')

    # 解密控件的实现
    def click_Decrypt(self):
        key = self.tab.passwd_text_3.toPlainText()
        p = self.tab.passwd_text_2.toPlainText()
        if self.tab.pushbutton_1.text() == "仿射加密":
            test = crypto.Radiate()
            TextPlain = test.decryption(p.encode(), key.encode())
            self.tab.passwd_text_1.setPlainText(TextPlain)
            self.send_Show_msg(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '：仿射解密成功!')
        elif self.tab.pushbutton_1.text() == "流密码加密":
            if self.tab.comboBox.currentIndex() == 1:
                test = crypto.cypto_LFSR(key)
                p = base64.b64decode(p)
                TextPlain = test.do_crypt(p)
                self.tab.passwd_text_1.setPlainText(TextPlain.decode())
                self.send_Show_msg(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '：LSFR_J-K解密成功!')
            elif self.tab.comboBox.currentIndex() == 0:
                test = crypto.RC4(key.encode())
                TextPlain = test.do_crypt(p.encode())
                self.tab.passwd_text_1.setPlainText(TextPlain.decode())
                self.send_Show_msg(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '：RC4解密成功!')
        elif self.tab.pushbutton_1.text() == "对称加密":
            p = bytes().fromhex(p)
            if self.tab.comboBox.currentIndex() == 0:
                test = crypto.des_crypto(key.encode())
                TextPlain = test.decrypt(p)
                self.tab.passwd_text_1.setPlainText(TextPlain.decode())
                self.send_Show_msg(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '：DES解密成功!')
            elif self.tab.comboBox.currentIndex() == 1:
                test = crypto.aes_crypto(key.encode())
                TextPlain = test.decrypt(p)
                self.tab.passwd_text_1.setPlainText(TextPlain.decode())
                self.send_Show_msg(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '：AES解密成功!')
        elif self.tab.pushbutton_1.text() == "非对称加密":
            p = p.split(' ')
            p.pop()
            temp = []
            for i in p:
                temp.append(int(int(i, 16)))
            print(temp)
            test = crypto.RSA()
            TextPlain = test.Decrypt(temp)
            self.tab.passwd_text_1.setPlainText(TextPlain)
            self.send_Show_msg(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '：RSA解密成功!')
        else:
            self.send_Show_msg(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '：请选择加密方式!')

    def ssl_start_server(self):
        self.ssl_server_thread = threading.Thread(target=self.ssl_server_recv)
        self.ssl_server_thread.start()
        msg = "服务器正在监听端口"
        self.send_Show_msg(msg)

    def ssl_start_client(self):
        self.ssl_client_thread = threading.Thread(target=self.ssl_client_recv)
        self.ssl_client_thread.start()

    def ssl_server_send(self):
        text = self.tab.tab5TextEdit_1.toPlainText()
        self.ssl_server_socket.sendall(text.encode())  # 回馈信息给客户端

    def ssl_client_send(self):
        inp = self.tab.tab5TextEdit_2.toPlainText()
        self.ssl_client_socket.sendall(inp.encode())

    def ssl_server_recv(self):
        ip_port = ('127.0.0.1', 9999)
        context = ssl.SSLContext(ssl.PROTOCOL_TLS)  # 创建了一个 SSL上下文,ssl.PROTOCOL_TLS表示选择客户端和服务器均支持的最高协议版本
        context.load_cert_chain(certfile="server.crt", keyfile="server.key")  # 加载一个私钥及对应的证书

        sk = socket.socket()  # 创建套接字
        sk.bind(ip_port)  # 绑定服务地址
        sk.listen(5)  # 监听连接请求

        msg = '#服务端消息#：启动socket服务，等待客户端连接...'
        self.send_Show_msg(msg)

        self.ssl_connect_sock, self.ssl_address = sk.accept()  # 等待连接，此处自动阻塞
        # 包装一个现有的 Python socket,并返回一个ssl socket,server_side为true表示为服务器行为，默认为false则表示客户端
        self.ssl_server_socket = context.wrap_socket(self.ssl_connect_sock, server_side=True)
        while True:  # 一个死循环
            client_data = self.ssl_server_socket.recv(1024).decode()  # 接收信息
            if client_data == 'exit':
                break
            self.tab.tab5TextEdit_1.clear()
            self.tab.tab5TextEdit_1.appendPlainText(client_data)
            msg = "#服务端消息#：收到来自%s的客户端发来的信息:%s" % (self.ssl_address, client_data)
            self.send_Show_msg(msg)

    def ssl_client_recv(self):
        context = ssl.SSLContext(ssl.PROTOCOL_TLS)  # 创建了一个 SSL上下文,ssl.PROTOCOL_TLS表示选择客户端和服务器均支持的最高协议版本
        context.verify_mode = ssl.CERT_REQUIRED  # 设置模式为CERT_REQUIRED，在此模式下，需要从套接字连接的另一端获取证书；如果未提供证书或验证失败则将引发 SSLError
        context.load_verify_locations("ca.crt")  # 加载一组用于验证其他对等方证书的CA证书

        ip_port = ('127.0.0.1', 9999)  # 设置端口
        s = socket.socket()  # 创建套接字
        # 包装一个现有的 Python 套接字 sock 并返回一个 SSLContext.sslsocket_class 的实例 (默认为 SSLSocket)。
        self.ssl_client_socket = context.wrap_socket(s, server_hostname='127.0.0.1')  # 返回的 SSL 套接字会绑定上下文、设置以及证书

        self.ssl_client_socket.connect(ip_port)  # 连接服务器
        msg = '#客户端消息#：客户端成功验证服务端证书，已成功连接，服务端证书信息如下'  # 输出证书信息
        self.send_Show_msg(msg)
        cert = pprint.pformat(self.ssl_client_socket.getpeercert())
        self.send_Show_msg(cert)
        msg = '请在文本框输入要发送的消息'
        self.send_Show_msg(msg)

        while True:  # 一个死循环
            server_data = self.ssl_client_socket.recv(1024).decode()  # 接收信息
            if server_data == 'exit':
                break
            self.tab.tab5TextEdit_2.clear()
            self.tab.tab5TextEdit_2.appendPlainText(server_data)
            msg = "#客户端消息#：收到来自%s的服务端发来的信息:%s" % (ip_port, server_data)
            self.send_Show_msg(msg)

    def click_Plain_clear(self):
        self.tab.passwd_text_1.clear()

    def click_Cipher_clear(self):
        self.tab.passwd_text_2.clear()

    def click_Setting_clear(self):
        self.tab.passwd_text_3.clear()

    def click_All_clear(self):
        self.tab.passwd_text_1.clear()
        self.tab.passwd_text_2.clear()
        self.tab.passwd_text_3.clear()

    def remove_serverText(self):
        self.tab.tab5TextEdit_1.clear()

    def remove_ClientText(self):
        self.tab.tab5TextEdit_2.clear()

    # 关闭线程
    def ssl_end_threading(self):
        self.ssl_server_socket.sendall('exit'.encode())
        self.ssl_client_socket.sendall('exit'.encode())
        msg = '客户端线程已关闭'
        self.send_Show_msg(msg)
        self.tab.tab5TextEdit_2.clear()
        msg = '服务端线程已关闭'
        self.send_Show_msg(msg)
        self.tab.tab5TextEdit_1.clear()
        self.ssl_server_socket.close()
        self.ssl_client_socket.close()
        msg = 'socket已关闭'
        self.send_Show_msg(msg)


def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = udp_logic()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
