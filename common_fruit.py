#!/usr/bin/env python
fruit1 = set()
fruit2 = set()
with open('DATA/fruit1.txt') as fruit1_in:
    for raw_line in fruit1_in:
        line = raw_line.rstrip()
        fruit1.add(line)
with open('DATA/fruit2.txt') as fruit2_in:
    for raw_line in fruit2_in:
        line = raw_line.rstrip()
        fruit2.add(line)

print("both:", fruit1 & fruit2)
fruit3 = set()
fruit4 = set()


with open('DATA/fruit1.txt') as fruit1_in:
    for raw_line in fruit1_in:
        line = raw_line.rstrip().lower()
        fruit3.add(line)
with open('DATA/fruit2.txt') as fruit2_in:
    for raw_line in fruit2_in:
        line = raw_line.rstrip().lower()
        fruit4.add(line)

print("both:", fruit3 & fruit4)