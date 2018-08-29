#!/usr/bin/env python
from pprint import pprint

data = [] # empty list

with open('Data/testscores.dat') as scores_in:
    for line in scores_in:
        # last_name, first_name, raw_score = line.rstrip().split(': |,')
        # data.append((last_name, first_name, int(raw_score)))
        name, raw_score = line.rstrip().split(':')
        data.append((name, int(raw_score)))
print(data)

with open('scorereport.txt','w') as report_out:
    for name, score in sorted(data):
        print(f"{name:20s}{score:2d}")
        report_out.write(f"{name:20s}{score:2d}\n")

