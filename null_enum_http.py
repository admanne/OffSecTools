#!/usr/bin/python
__author__ = 'admanne'
import sys
import os

if len(sys.argv) != 3:
    print "<address> <port>"
    sys.exit(0)

address = sys.argv[1].strip()
port = sys.argv[2].strip()
# Enum
os.system(
    "xterm -e \"nmap -sV -Pn -vv -p %s --script=http-huawei-hg5xx-vuln.nse,http-iis-webdav-vuln.nse,http-vmware-path-vuln.nse,http-vuln-cve2009-3960.nse,"
    "http-vuln-cve2010-0738.nse,http-vuln-cve2010-2861.nse,http-vuln-cve2011-3192.nse,http-vuln-cve2011-3368.nse,http-vuln-cve2012-1823.nse,"
    "http-vuln-cve2013-0156.nse -oX 'enum_http_%s.xml' %s\"" % (
        port, address, address))