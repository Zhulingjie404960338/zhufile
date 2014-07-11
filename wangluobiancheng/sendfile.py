#coding=utf-8
'''
Created on 2014Äê7ÔÂ10ÈÕ

@author: SSD
'''
from socket import *

import os

import struct

ADDR = ('172.16.10.99',8000)

BUFSIZE = 1024

filename = '/root/test'

FILEINFO_SIZE=struct.calcsize('128s32sI8s')

sendSock = socket(AF_INET,SOCK_STREAM)

sendSock.connect(ADDR)

fhead=struct.pack('128s11I',filename,0,0,0,0,0,0,0,0,os.stat(filename).st_size,0,0)

sendSock.send(fhead)

fp = open(filename,'rb')

while 1:

    filedata = fp.read(BUFSIZE)

    if not filedata: 
        break

    sendSock.send(filedata)

fp.close()

sendSock.close()