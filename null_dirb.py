#!/usr/bin/python
#
__author__ = 'admanne'
import os
import os.path
import sys
import datetime
import time
import threading

if len(sys.argv) != 2:
    print "Usage: dirbust.py <targets>"
    sys.exit(0)

targets = str(sys.argv[1])
folders = ["/usr/share/dirb/wordlists/", "/usr/share/dirb/wordlists/vulns/"]

def dirb_thread(command_chain, blank):
    os.system(command_chain)

out_put_files = []

f = [line.strip() for line in open(targets)]
for address in f:
    command_chain=""
    print "INFO: Starting dirb scan for " + address
    for folder in folders:
        for wordfile in os.listdir(folder):
            wordlist = folder+wordfile
            if wordlist[-3:] == "txt":
                outfile = str(address)+str("-dirb.txt")
                url = "http://"+address
                out_put_files.append(outfile)
                command_chain += "xterm -e \"dirb %s %s -o %s -r \"; " % (url, wordlist, outfile)
            # t = threading.Thread(target=dirb_thread, args=(command_chain, ""))
            # t.start()

def dirb_analyze():
    out_put_files = list(set(out_put_files))
    for f in out_put_files:
        print(f)

    #cat 192.168.15.224\:80-dirb.txt | grep DIRECTORY | sort -u
    #cat 192.168.15.224\:80-dirb.txt | grep + | sort -u
dirb_analyze()