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

def by_color(k):
    return k[1][1]

def by_color_title(k):
    return k[1][1], k[1][0]

for name, info in sorted(data.items(),key=by_color_title):
    title, color, quest, comment = info
    print(title,name,color)