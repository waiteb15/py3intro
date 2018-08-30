#!/usr/bin/env python

"""Basic sorting example"""
fruit = ["pomegranate", "cherry", "apricot", "date", "Apple", "lemon", "Kiwi",
"ORANGE", "lime", "Watermelon", "guava", "papaya", "FIG", "pear", "banana",
"Tamarind", "persimmon", "elderberry", "peach", "BLUEberry", "lychee",
 "grape" ]

sorted_fruit = sorted(fruit) # <1>

print(sorted_fruit, '\n')

def ignore_case(fruit):
    return fruit.lower()

# "key" means "key function"
f1 = sorted(fruit, key=ignore_case)
print("f1:", f1, '\n')

f2 = sorted(fruit, key=str.lower)
print("f1:", f2, '\n')

f3 = sorted(fruit, key=len)
print("f3:", f3, '\n')

def custom_sort1(item):
    return len(item), item.lower()

f4 = sorted(fruit,key=custom_sort1)
print("f4:", f4, '\n')

def custom_sort2(item):
    return item[-1]

f5 = sorted(fruit, key = custom_sort2)

print("f5:",fruit,'\n')

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

def last_name_sort(t):
    return t[1], t[0]

for first_name, last_name, item in sorted(people,key=last_name_sort):
    print(last_name,',',first_name)



def by_value(item):
    return item[1], item[0]

airports = { 'IAD': 'Dulles', 'SEA': 'Seattle-Tacoma',
       'RDU': 'Raleigh-Durham', 'LAX': 'Los Angeles' }

#dictionary needs the .items()
for abbr, name in sorted(airports.items(),key=by_value):
    print(name, abbr)

for abbr, name in sorted(airports.items(), key=lambda i: (i[1], i[0])):
    print(name, abbr)

f6 = sorted(fruit, key = lambda f: f.lower())
print("f6", f6)

f7 = sorted(fruit, key= str.lower, reverse=True)
print(f7)

fruit.sort(key=str.lower)
print(fruit ,'\n')