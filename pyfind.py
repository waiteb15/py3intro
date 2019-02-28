#!/usr/bin/env python

import sys
import re

pattern = sys.argv[1]
files = sys.argv[2:]

for file in files:
    print(f"\nSearching for {pattern} in {file}\n")
    with open(file) as file_in:
        for line in file_in:
            if re.search(pattern, line, re.I):
                print(line.rstrip())
