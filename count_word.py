#!/usr/bin/env python

import sys

count = 0

word = str(sys.argv[1])

with open('DATA/alice.txt') as alice_in:
        for raw_line in alice_in:
            if word in raw_line:
                count += 1


print(f"There are {count} lines with the word '{word}' in them")