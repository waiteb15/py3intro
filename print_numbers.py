#!/usr/bin/env python
import re

#  \d   [0-9]
pattern = r"\b(?:\d{3}-)?\d{3}-\d{4}\b"

with open('DATA/custinfo.dat') as cust_in:
    text = cust_in.read()
    print(re.findall(pattern, text))

