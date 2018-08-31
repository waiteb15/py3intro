#!/usr/bin/env python

import sys
import os

for file in sys.argv[1:]:
    try:
        print(f'{file} is {os.path.getsize(file)} bytes')
    except Exception:
        print("FILE DOES NOT EXIST!!!")