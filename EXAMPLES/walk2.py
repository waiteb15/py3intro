#!/usr/bin/env python

"""
    find files whose size is greater than 1000 bytes
"""
import sys
import os

if len(sys.argv) < 2:
    print('Syntax: walk2.py START-DIR')
    sys.exit(1)

for currdir, subdirs, files in os.walk(sys.argv[1]):
    for file in files:
        fullpath = os.path.join(currdir, file)
        if os.path.isfile(fullpath):
            fsize = os.path.getsize(fullpath)
            if fsize > 1000:
                print("{:40s} {:8d}".format(fullpath, fsize))
