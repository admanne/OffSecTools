#!/usr/bin/python
# __author__ = 'mannea'
#
import sys
import os

if len(sys.argv) != 3:
    print "aasplit <in file> <number of files>"
    sys.exit(0)

in_file = sys.argv[1].strip()
split_lines = sys.argv[2].strip()


current_dir = os.popen('pwd').read().rstrip()

file_lines = sum(1 for line in open(in_file))

new_lines = (int(float(file_lines)) / int(float(split_lines)))

os.system("split -d --verbose -l %s %s %s" % (new_lines, in_file, in_file))