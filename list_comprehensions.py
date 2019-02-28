#!/usr/bin/env python

fruits = ["pomegranate", "  cherry", "apricot", "date", "apple",
"lemon", "kiwi", "orange", "lime  ", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "  blueberry", "lychee", "grape" ]

f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0:", f0, '\n')

f1 = [f.upper() for f in fruits]
# [EXPR for VAR ... in ITERABLE if COND]
print("f1:", f1, '\n')

f2 = [f.upper() for f in fruits if f.lower().startswith('p')]
print("f2:", f2, '\n')

f3 = [f for f in fruits if f.lower().startswith('p')]
print("f3:", f3, '\n')

food = ['eggs', 'eggs', 'spam', 'spam', 'spam', 'spam',
        'spam', 'spam', 'spam', 'spam', 'spam',
        'spam', 'spam', 'spam', 'spam', 'spam',
        'spam', 'spam', 'spam', 'spam', 'toast',
        'cheeseburger', 'spam', 'spam', 'spam', ]

food2 = [f for f in food if f != 'spam']
print("food2:", food2, '\n')

f4 = [f.upper().strip() for f in fruits]
print("f4:", f4, '\n')

def doit(x):
    print("Doing things")
    return x.upper().strip()[:3]

f5 = [doit(f) for f in fruits]
print("f5:", f5, '\n')

#   perl -i.BAK -pe 's/foo/bar/g;' *.txt

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

first_names = [p[0] for p in people]
print("first_names:", first_names, '\n')

names = [f"{p[0]} {p[1]}" for p in people if p[1][0] > 'E']
print("names:", names, '\n')
