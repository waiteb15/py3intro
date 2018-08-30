#!/usr/bin/env python

fruits = []
with open('DATA/fruit.txt') as fruit_in:
    for line in fruit_in:
        fruits.append(line.rstrip())

print(fruits)

print('case-sensitive',sorted(fruits),'\n')


print('case-insensitive',sorted(fruits,key = str.lower),'\n')

print('length then name',sorted(fruits,key = lambda i: (len(i), i[0])),'\n')

print('2nd letter than letter (case insensitive) ',sorted(fruits,key = lambda i: (i[1].lower(), i[0].lower())),'\n')


