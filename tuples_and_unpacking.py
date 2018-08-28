#!/usr/bin/env python

import numpy as np
#what is a tuple?
#
# fixed size collection of related data
# read-only once created
# designed to kinda/sorta be like structures in C/C++
# non-descructive list operations work with tuples

person = "Tom", "Hanks", 56

# print(len(person))
# print(person[2])

# var1, var2, ... = ITERABLE
# we can upack iterables in python
first_name, last_name, age = person
newlist = ["done", "abort", "failed"]
done, abort, fail = newlist
#print(fail)

###nested

people = [
    ('Melinda', 'Gates', 'Gates Foundation'),
    ('Steve', 'Jobs', 'Apple'),
    ('Larry', 'Wall', 'Perl'),
    ('Paul', 'Allen', 'Microsoft'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Bill', 'Gates', 'Microsoft'),
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Sergey','Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linus', 'Torvalds', 'Linux'),
]

for person in people:   # <1>
    print(person[0], person[1])
print('-' * 60)

for person in people:
    first_name, last_name, product = person  # <2>
    print(first_name, last_name)
print('-' * 60)

for first_name, last_name, product in people:  # <3>
    print(first_name, last_name)
print('-' * 60)

pep_boys = ["man", "moe", "jack"]
print(list(enumerate(pep_boys)))
for i, boy in enumerate(pep_boys):
    print(i,boy)
print('-' * 60)

print('-' * 60)
for i, boy in enumerate(pep_boys):
    print(i,boy)
places = [('Troy', 'NY'), ('Albany','NY')]
print('-' * 60)
for city, state  in places:
     print(city, state)
print('-' * 60)
pb = pep_boys
print(pb)
print(len(pb))
print(min(pb))
print(max(pb))
print(sorted(pb))
print(list(reversed(pb)))
print('-' * 60)

x = ['a','b','c']
y = [5, 10, 15]
m = list(zip(x, y, pep_boys))
print(m*2)
print(places * 8)

# n = np.zeros(1000, dtype =np.uint16)
# n.shape = [10, 10, 10, ]
# print(n)

for i in range(5, 101, 5):
    print(i)