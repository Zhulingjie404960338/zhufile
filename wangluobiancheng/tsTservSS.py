#coding=utf-8
#从SockServer导入需要的类
from SocketServer import (TCPServer as TCP, StreamRequestHandler as SRH) 
from time import ctime 
HOST = '' 
PORT = 21567 
ADDR = (HOST, PORT) 
#从SocketServer的StreamRequestHandler类中派生一个子类，并重写handle（）函数，在StreamRequestHandler类中handle（）函数什么都没做，在消息进来时，handle()函数就会被调用
class MyRequestHandler(SRH): 
    def handle(self): 
        print '...connected from:', self.client_address 
        #readline（）函数得到客户消息，write()函数把字符串发送给客户
        self.wfile.write('[%s] %s' % (ctime(), self.rfile.readline())) 
tcpServ = TCP(ADDR, MyRequestHandler) 
print 'waiting for connection...'
#进入等待客户请求与处理客户请求的无限循环中 
tcpServ.serve_forever() 