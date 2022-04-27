#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ref website
# https://shengyu7697.github.io/python-udp-socket/

import socket
import time

HOST = '0.0.0.0'
PORT = 7000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))

print('server start at: %s:%s' % (HOST, PORT))
print('wait for connection...')

while True:
    indata, addr = s.recvfrom(1024)
    print('recvfrom ' + str(addr) + ': ' + indata.decode())
    sendingTime = time.time()
    outdata = 'echo ' + indata.decode() + f', resentTime: {sendingTime}'
    s.sendto(outdata.encode(), addr)