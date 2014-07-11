#coding=utf-8
from socket import * 
HOST = 'localhost' 
PORT = 21567 
BUFSIZ = 1024 
ADDR = (HOST, PORT) 
udpCliSock = socket(AF_INET, SOCK_DGRAM) 
#通讯循环与TCP基本相同，但不用与服务器建立连接，直接把消息发送出去
while True: 
    data = raw_input('> ') 
    if not data: 
        break 
    udpCliSock.sendto(data, ADDR) 
    data, ADDR = udpCliSock.recvfrom(BUFSIZ) 
    if not data: 
        break 
    print data
udpCliSock.close() 