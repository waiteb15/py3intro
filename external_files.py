#!/usr/bin/env python
import os

os.system('netstat -an')
# os.system('/path/to/my/fortran/utility.exe /path/to/my/data/file')
print('-' * 60)

with os.popen('netstat -an') as netstat_in:
    print(netstat_in)
    for line in netstat_in:
        if "ESTABLISHED" in line:
            print(line.rstrip())
