#!/usr/bin/env python

values = ['a', 'b', 'c']

i = 0
for value in values:
    print(i, value)
    i = i + 1

print()

for i, value in enumerate(values):
    print(i, value)
print()

print(list(enumerate(values)))

print(values.index('b'))

x = 5
y = 10

print(f"{x:10s} {y:20s}")  # >= 3.6
print("{:10s} {:20s}".format(x, y))  # < 3.6



