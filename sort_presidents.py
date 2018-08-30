#!/usr/bin/env python

presidents = []

with open('DATA/presidents.txt') as presi_in:
    for line in presi_in:
        presidents.append(line.rstrip().split(':'))


for val in sorted(presidents,key=lambda i: (i[1],i[2])):
    print(f'{val[2]:25s}{val[1]:20s}:{val[6]:10s}')

