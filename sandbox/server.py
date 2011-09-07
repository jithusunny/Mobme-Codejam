#!/usr/bin/python

#Filename: server.py
#Author: Jithu Sunny
#Date: June 19, 2011

from socket import *
import commands, sys, string, time

data = ''
host = ''
port = int(sys.argv[1])
buf = 4092

server = socket(AF_INET, SOCK_STREAM)

server.bind((host, port))
server.listen(1)

print 'Listening...'

client, addr = server.accept()
ip = client.getpeername()[0]
port = client.getpeername()[1]

print 'Connnection with port', port, 'of client with ip', ip, 'established..!'
while 1:
    data = client.recv(buf).strip().split()
    
    if data:
        command = data[0]

        if command == 'quit':
            client.close()
            break

        elif command == 'ls':
            returnval, output = commands.getstatusoutput('ls')

            if returnval:
	        client.send('Error..!')
            else:
                client.send(output)

        elif command == 'pwd':
            returnval, output = commands.getstatusoutput('pwd')

            if returnval:
                client.send('Error..!')
            else:
                client.send(output)

        elif command == 'cat':
            returnval, output = commands.getstatusoutput('cat ' + str(data[1]))

            if returnval:
	        client.send('Error..!')
            else:
                client.send(output)

        elif command == 'rm':
            returnval, output = commands.getstatusoutput('rm ' + str(data[1]))

            if returnval:
                client.send('Error..!')
            else:
                client.send('Done..!')

        elif command == 'touch':
            returnval, output = commands.getstatusoutput('touch ' + data[1])

            if returnval:
                client.send('Error..!')
            else:
                filename = data[1]
                data = data[2:]
                contents = string.join(data)
                fp = open(filename, 'w')
                fp.write(contents)
                fp.close()
                client.send('Done..!')

        elif command == 'time':
            localtime = time.localtime()
            servertime = str(localtime.tm_hour) + ':' + str(localtime.tm_min) + ':' + str(localtime.tm_sec)
            client.send(servertime)

        else:
            client.send('Invalid command')

print 'Client connection terminated..!'
server.close()
