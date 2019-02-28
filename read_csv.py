#!/usr/bin/env python
import csv

with open('DATA/knights.csv') as knights_in:
    rdr = csv.reader(knights_in)
    for row in rdr:
        print(row)
print('-' * 60)

with open('DATA/knights.txt') as knights_in:
    rdr = csv.reader(knights_in, delimiter=':')
    for row in rdr:
        print(row)
