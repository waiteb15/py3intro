#!/usr/bin/env python

from pprint import pprint
data = {}

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(":")
        data[name] = title, color, quest, comment

print(data['Galahad'][2])
print(data['Robin'])
title, color, quest, comment = data['Lancelot']


for name, (title, color, quest, comment) in data.items():
    print(title,name)


