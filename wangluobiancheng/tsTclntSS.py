#coding=utf-8
from socket import * 
HOST = 'localhost' 
PORT = 21567 
BUFSIZ = 1024 
ADDR = (HOST, PORT) 
#SocketServer 的请求处理器的默认行为是接受连接，得到请求，然后就关闭连接。要每次发送数据到服务器的时候都要创建一个新的套接字
while True: 
    tcpCliSock = socket(AF_INET, SOCK_STREAM) 
    tcpCliSock.connect(ADDR) 
    data = raw_input('> ') 
    if not data: 
        break 
    #我们使用的处理器类像文件一样操作套接字，所以我们每次都要发送行结束字符（回车与换行），服务器只是保留并重用我们发送的行结束字符。当我们从服务器得到数据的时候，我们使用 strip()函数去掉它们，然后使用 print 语句提供的回车。
    tcpCliSock.send('%s\r\n' % data) 
    data = tcpCliSock.recv(BUFSIZ) 
    if not data: 
        break 
    print data.strip() 
tcpCliSock.close() 