#!/usr/bin/env python

#This method is preferable when files are large
with open("DATA/mary.txt","r") as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip() #.rstrip('\n\r')
        print(line)

print("--"*30)
with open("DATA/mary.txt","r") as mary_in:
    all_text = mary_in.read() # entire file
    print(all_text[:100])

print("--"*30)
# if you want \n
with open("DATA/mary.txt","r") as mary_in:
    all_lines = mary_in.readlines() # entire file
    print(all_lines)

print("--"*30)
#mary_in is an iterable (generator)
# if you want the clean lines
with open("DATA/mary.txt") as mary_in:
    all_lines = [line.rstrip() for line in mary_in]
    print(all_lines)


