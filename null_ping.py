#!/usr/bin/python
__author__ = 'admanne'
import sys
import os

if len(sys.argv) != 2:
    print "null_ping <range>"
    print "null_ping 192.168.1.1-255"
    sys.exit(0)

addr = sys.argv[1].strip()

cmd = 'nmap -sP ' +str(addr)
os.system(cmd)