#!/usr/bin/env python
from pprint import pprint
import re

data = []  # empty list

with open('DATA/testscores.dat') as scores_in:
    for line in scores_in:
        last_name, first_name, raw_score = re.split(r'(?:,\s*|:)',line.rstrip())
        data.append((last_name, first_name, int(raw_score)))

with open('scorereport.txt', """w""") as report_out:
    for last_name, first_name, score in sorted(data):
        print(f"{first_name:20s} {last_name:20s} {score:2d}")
        report_out.write(f"{first_name:20s} {last_name:20s} {score:2d}")
