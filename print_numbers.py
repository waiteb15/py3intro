#!/usr/bin/env python
import re

with open('DATA/custinfo.dat') as cust_in:
    for raw_line in cust_in:
        if re.search(r'\b\d{3}-\d{4}\b', raw_line):
            print(raw_line.rstrip())
        # else:
        #     print("no number")