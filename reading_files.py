#!/usr/bin/env python

with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()   # .rstrip('\n\r')
        print(line.upper())
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    all_text = mary_in.read()
    print(all_text[:75])
print('-' * 60)

# if you want the '\n'
with open('DATA/mary.txt') as mary_in:
    all_lines = mary_in.readlines()
    print(all_lines)
print('-' * 60)

# if you DON'T want the '\n'
with open('DATA/mary.txt') as mary_in:
    all_lines = [line.rstrip() for line in mary_in]
    print(all_lines)



# my_path = '/fun/tools/for/newbies.txt'

