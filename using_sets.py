#!/usr/bin/env python

john_countries = """Mexico
Barbados
China
Canada
UK
Austria
Spain
Bulgaria
Israel""".split('\n')

clare_countries = """British Virgin Islands
Denmark
UK
Spain
Kenya
Mexico
Barbados
Norway
Sweden
Canada""".split('\n')


john = set(john_countries)
clare = set(clare_countries)

for i in range(1000000):
    john.add('France')

print("both:", john & clare)
print("either:", john | clare)
print("just one:", john ^ clare)
print("just John:", john - clare)
print("just Clare:", clare - john)

with open('DATA/breakfast.txt') as breakfast_in:
    food = [b.rstrip() for b in breakfast_in]
    food_set = set(food)
    print(food_set)
print()

print(sorted(john))
j = set(sorted(john))
print(j)







