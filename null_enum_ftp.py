#!/usr/bin/python
__author__ = 'admanne'
import sys
import os

if len(sys.argv) != 3:
    print "<address> <port>"
    sys.exit(0)


address = sys.argv[1].strip()
port = sys.argv[2].strip()
#Enum
os.system("xterm -e \"nmap -sV -Pn -vv -p %s --script=ftp-anon,ftp-bounce,ftp-libopie,ftp-proftpd-backdoor,ftp-vsftpd-backdoor,ftp-vuln-cve2010-4221 -oX 'enum_ftp_%s.xml' %s\"" % (port,address,address))