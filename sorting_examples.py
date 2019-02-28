#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "date", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE" ]

f0 = sorted(fruits)
print("f0:", f0, '\n')

def ignore_case(fruit):
    # print(fruit)
    return fruit.lower()



# "key" means "key function"
f1 = sorted(fruits, key=ignore_case)
print("f1:", f1, '\n')

f2 = sorted(fruits, key=str.lower)
print("f2:", f2, '\n')

f3 = sorted(fruits, key=len)
print("f3:", f3, '\n')

def custom_sort1(item):
    return len(item), item.lower()

f4 = sorted(fruits, key=custom_sort1)
print("f4:", f4, '\n')

def custom_sort2(item):
    return item[-1]

f5 = sorted(fruits, key=custom_sort2)
print("f5:", f5, '\n')

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

for first_name, last_name, product in sorted(people):
    print(first_name, last_name)
print('-' * 60)

def last_name_sort(person):
    return person[1], person[0]

for first_name, last_name, product in sorted(people, key=last_name_sort):
    print(first_name, last_name)
print('-' * 60)



airports = {
    'EWR': 'Newark',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SAC': 'Sacramento',
    'IAD': 'Dulles',
}
print(airports.items())
print()

for abbr, name in sorted(airports.items()):
    print(abbr, name)
print()

def by_value(item):
    return item[1], item[0]

for abbr, name in sorted(airports.items(), key=by_value):
    print(abbr, name)
print()

for abbr, name in sorted(airports.items(), key=lambda i: (i[1], i[0])):
    print(abbr, name)
print()

f6 = sorted(fruits, key=lambda f: f.lower())
print("f6:", f6, '\n')

f7 = sorted(fruits, key=str.lower, reverse=True)
print("f7:", f7, '\n')

fruits.sort(key=str.lower)
print(fruits)


