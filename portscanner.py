#!/usr/bin/python3
import socket,sys
address = sys.argv[1]
s = socket.socket()
for i in range(0,65535):
    try:
        s.connect((address, i))
        print(i,"open")
    except Exception as e: 
       pass
