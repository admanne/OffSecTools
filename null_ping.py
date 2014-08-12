#!/usr/bin/python
__author__ = 'admanne'
import sys
import os

if len(sys.argv) != 4:
    print "null_ping <subnet> <start> <stop>"
    sys.exit(0)

subnet = sys.argv[1].strip()
start = int(sys.argv[2].strip())
stop = int(sys.argv[3].strip())

for x in range(start, stop):
    addr = str(subnet)+str(x)
    print addr
    cmd = 'ping -W 3 -c 1 ' +str(addr)
    os.system(cmd)