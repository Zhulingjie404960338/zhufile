#coding=utf-8
#启动信息。导入socket模块所有属性
from socket import *
#需要连接的服务器地址 ，端口号需要与服务器上的设置相同
HOST = 'localhost' 
PORT = 21567 
#缓冲区大小设为1K
BUFSIZ = 1024 
ADDR = (HOST, PORT) 
#创建套接字并连接服务器
tcpCliSock = socket(AF_INET, SOCK_STREAM) 
tcpCliSock.connect(ADDR) 
#通讯循环
while True: 
    data = raw_input('> ') 
    #用户没有输入任何内容时退出
    if not data: 
        break 
    tcpCliSock.send(data) 
    #服务器由于某种原因退出，导致热词V（）函数失败时退出
    data = tcpCliSock.recv(BUFSIZ) 
    if not data: 
        break 
    print data 
tcpCliSock.close() 