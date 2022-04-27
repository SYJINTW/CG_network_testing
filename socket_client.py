#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ref website
# https://shengyu7697.github.io/python-udp-socket/

import socket

HOST = '140.114.79.84'
PORT = 7000
server_addr = (HOST, PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    outdata = input('please input message: ')
    print('sendto ' + str(server_addr) + ': ' + outdata)
    s.sendto(outdata.encode(), server_addr)
    
    indata, addr = s.recvfrom(1024)
    print('recvfrom ' + str(addr) + ': ' + indata.decode())
