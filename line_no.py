#!/usr/bin/env python

#8/29/18


import sys

for i in range(1,len(sys.argv)):
    filename = str(sys.argv[i])
    print(f"\n printing {filename} \n")
    with open(filename) as file_in:
        for j, raw_line in enumerate(file_in,1):
            line = raw_line.rstrip() # .rstrip('\n\r')
            print(j, line)


