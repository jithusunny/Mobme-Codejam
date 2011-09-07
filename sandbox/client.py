#!/usr/bin/python

#Filename: client.py
#Author: Jithu Sunny
#Date: June 19, 2011

from socket import *
import sys

host = ''
port = int(sys.argv[1])
buf = 4096

cli = socket(AF_INET, SOCK_STREAM)

cli.connect((host, port))

cli.send('pwd')
path = cli.recv(buf)

prompt = 'Server Port ' + str(port) + ':~/-' + path + ': ' 

while 1:
    request = raw_input(prompt)
    cli.send(request)
    data = cli.recv(buf)
    if request == 'quit':
        cli.close()
        break
    print data
