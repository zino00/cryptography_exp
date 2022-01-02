import threading
import socket
import ssl
import pprint
from PyQt5 import QtWidgets
import UI
import sys

class SSL(UI.MainUi):
    def __init__(self):
        # 调用父类的init函数
        super(SSL, self).__init__()
        self.ssl_client_socket = None
        self.ssl_server_socket = None
        self.ssl_connect_sock = None
        self.ssl_address = None
        self.ssl_server_thread = None
        self.ssl_client_thread = None

    def ssl_start_server(self):
        self.ssl_server_thread = threading.Thread(target=self.ssl_server_recv)
        self.ssl_server_thread.start()
        msg = "服务器正在监听端口"
        self.send_Show_msg(msg)
        print(msg)

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
        print(msg)
        self.ssl_connect_sock, self.ssl_address = sk.accept()  # 等待连接，此处自动阻塞
        # 包装一个现有的 Python socket,并返回一个ssl socket,server_side为true表示为服务器行为，默认为false则表示客户端
        self.ssl_server_socket = context.wrap_socket(self.ssl_connect_sock, server_side=True)
        while True:  # 一个死循环
            client_data = self.ssl_server_socket.recv(1024).decode()  # 接收信息
            self.tab.tab5TextEdit_1.setPlainText(client_data)
            msg = "#服务端消息#：收到来自%s的客户端发来的信息:%s" % (self.ssl_address, client_data)
            self.send_Show_msg(msg)


    def ssl_client_recv(self):
        context = ssl.SSLContext(ssl.PROTOCOL_TLS)  # 创建了一个 SSL上下文,ssl.PROTOCOL_TLS表示选择客户端和服务器均支持的最高协议版本
        context.verify_mode = ssl.CERT_REQUIRED  # 设置模式为CERT_REQUIRED，在此模式下，需要从套接字连接的另一端获取证书；如果未提供证书或验证失败则将引发 SSLError
        context.load_verify_locations("ca.crt")  # 加载一组用于验证其他对等方证书的CA证书

        ip_port = ('127.0.0.1', 9999)  # 设置端口
        s = socket.socket()  # 创建套接字
        # 包装一个现有的 Python 套接字 sock 并返回一个 SSLContext.sslsocket_class 的实例 (默认为 SSLSocket)。
        self.ssl_client_socket = context.wrap_socket(s, server_hostname='127.0.0.1')# 返回的 SSL 套接字会绑定上下文、设置以及证书

        self.ssl_client_socket.connect(ip_port)  # 连接服务器
        msg = '#客户端消息#：客户端成功验证服务端证书，已成功连接，服务端证书信息如下,请输入要发送的消息'  # 输出证书信息
        self.send_Show_msg(msg)
        print('#客户端消息#：客户端成功验证服务端证书，已成功连接，服务端证书信息如下')
        # cert = None
        pprint.pprint(self.ssl_client_socket.getpeercert())
        # print(type(self.ssl_client_socket.getpeercert()))
        # print(cert)
        # self.send_Show_msg(cert)
        while True:  # 一个死循环
            server_data = self.ssl_client_socket.recv(1024).decode()  # 接收信息
            self.tab.tab5TextEdit_2.setPlainText(server_data)
            msg = "#客户端消息#：收到来自%s的服务端发来的信息:%s" % (ip_port, server_data)
            self.send_Show_msg(msg)


    def remove_serverText(self):
        self.tab.tab5TextEdit_1.clear()

    def remove_ClientText(self):
        self.tab.tab5TextEdit_2.clear()


def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = SSL()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()




