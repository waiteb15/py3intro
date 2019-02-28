#!/usr/bin/env python
import numpy as np

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
    ('Linus', 'Torvalds', 'Linux', "Git"),
]
print(people[0][0][0])

for person in people:
    first_name, last_name, *product = person
    print(first_name, last_name, product)
print('-' * 60)

for first_name, last_name, *product in people:
    print(first_name, last_name, product)
print('-' * 60)

pep_boys = ["Manny", "Moe", "Jack"]

e = enumerate(pep_boys)
print(e)
print(list(e))

for i, boy in enumerate(pep_boys):
    print(i, boy)
print()

places = [('Detroit', 'MI'), ('Pittsburgh', 'PA'),
          ('Canandaigua', 'NY')]

for i, (city, state) in enumerate(places, 1):

    print("{} {:15s} {}".format(i, city, state))
    print(f"{i} {city:15s} {state}")

print('-' * 60)
print(pep_boys)
pb = pep_boys

print(len(pb))
print(min(pb))
print(max(pb))
print(sorted(pb))
print(list(reversed(pb)))

x = ['a', 'b', 'c']
y = [5, 10, 15, 20, 25]

m = zip(x, y, pep_boys)
print(m)
print(list(m))

print(pep_boys * 3)
flags = [0] * 10
print(flags)
print("BRAD PITT-" * 10)

r = range(10)
print(r)
#  range(STOP)  range(START, STOP) range(START, STOP, STEP)
for i in range(5):
    print(i)

# n = np.zeros(1000000, dtype=np.uint16)
# n.shape = (2, 5, 10, 10, 1000)
# print(n)
print()

for i in range(5, 101, 5):
    print(i)

