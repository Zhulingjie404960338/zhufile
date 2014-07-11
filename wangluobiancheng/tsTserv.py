#coding=utf-8
#启动信息，导入time.ctime()函数和socket模块的所有属性
from socket import * 
from time import ctime 
#HOST为空，bind（）函数绑定到所有有效地址上
HOST = '' 
#选择一个未被占用的端口
PORT = 21567 
#缓冲大小设为1K，可根据网络情况及应用需求修改大小
BUFSIZ = 1024 
ADDR = (HOST, PORT) 
#生成套接字并绑定到地址上
tcpSerSock = socket(AF_INET, SOCK_STREAM) 
tcpSerSock.bind(ADDR) 
#最多允许多少个连接同时接入，后来的连接将被拒绝
tcpSerSock.listen(5) 
#进入服务器无限循环
while True: 
    #被动等待连接到来
    print 'waiting for connection...' 
    tcpCliSock, addr = tcpSerSock.accept() 
    print '...connected from:', addr 
    while True: 
        data = tcpCliSock.recv(BUFSIZ) 
        #消息为空，客户退出，等待下一个客户的连接
        if not data: 
            break 
        #得到消息后在消息前加一个时间戳后返回信息
        tcpCliSock.send('[%s] %s' % (ctime(), data)) 
    tcpCliSock.close()
#不会被执行到，提醒服务器退出时调用。close（）函数 
tcpSerSock.close() 