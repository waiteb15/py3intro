#!/usr/bin/env python

from collections import Counter


shell_info= {}
with open('DATA/passwd') as passwd_in:
    for raw_line in passwd_in:
        (a, b, c, d, e, f, shell) = raw_line.rstrip().split(':')
        if shell =="":
            shell = 'NONE'
        if shell in shell_info:
            shell_info[shell] = shell_info[shell] + 1
        else:
            shell_info[shell] = 1

for item, count in shell_info.items():
    print(item, count)