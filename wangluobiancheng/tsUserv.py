#coding=utf-8
#启动信息，导入time.ctime()函数和socket模块的所有属性
from socket import * 
from time import ctime 
HOST = '' 
PORT = 21567 
BUFSIZ = 1024 
ADDR = (HOST, PORT) 
#socket（）函数使用UDP套接字类型，bind（）与TCP相同，由于UDP是无连接的，不用调用listen（）函数监听连接
udpSerSock = socket(AF_INET, SOCK_DGRAM) 
udpSerSock.bind(ADDR) 
#进入服务器无限循环
while True: 
    print 'waiting for message...' 
    data, addr = udpSerSock.recvfrom(BUFSIZ) 
    udpSerSock.sendto('[%s] %s' % (ctime(), data), addr) 
    print '...received from and returned to:', addr 
#不会被执行到，提醒服务器退出时调用。close（）函数 
udpSerSock.close() 