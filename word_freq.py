#!/usr/bin/env python
import re
import sys

file_name = sys.argv[1]
rx_wordsep = re.compile(r"[^\w']+")
with open(file_name) as file_in:
    words = rx_wordsep.split(file_in.read())

print(words)


