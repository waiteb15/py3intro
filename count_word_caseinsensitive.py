#!/usr/bin/env python

import sys


word = str(sys.argv[1])
file_name = sys.argv[2:]


for file in file_name:
    count = 0
    count_exact = 0
    print(f"\nlooking for '{word}' case insensitive in {file}\n")
    with open(file) as file_in:
        for raw_line in file_in:
             if word.lower() in raw_line.lower():
                  count += 1
             if word in raw_line:
                 count_exact += 1
    print(f"There are {count} lines with the case insenstive word '{word}' in them \n "
        f" but only {count_exact} lines with exact word '{word}' in them")