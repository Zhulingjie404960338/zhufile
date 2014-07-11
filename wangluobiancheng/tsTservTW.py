#coding=utf-8
'''
Created on 2014Äê7ÔÂ11ÈÕ

@author: SSD
'''
from twisted.internet import protocol, reactor 
from time import ctime 
PORT = 21567 
class TSServProtocol(protocol.Protocol): 
    def connectionMade(self): 
        clnt = self.clnt = self.transport.getPeer().host 
        print '...connected from:', clnt 
    def dataReceived(self, data): 
        self.transport.write('[%s] %s' % ( ctime(), data)) 
factory = protocol.Factory() 
factory.protocol = TSServProtocol 
print 'waiting for connection...' 
reactor.listenTCP(PORT, factory) 
reactor.run() 