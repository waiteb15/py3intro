#!/usr/bin/env python

#!/usr/bin/env python

fruits = ['watermelon', 'apple', 'mango', 'kiwi', 'apricot', 'lemon', 'guava']

f0 = []

for f in fruits:
    f0.append(f.upper())

print("f0",f0,'\n')


# LIST COMPREHENSION [ EXP FOR VAR .. ITERABLE (OPT IN COND]
f1 = (f.upper() for f in fruits)
print("f1",f1,'\n')

f2 = (f.upper() for f in fruits if f.lower().startswith('a'))
print("f2",f2,'\n')


f3 = (f for f in fruits if f.lower().startswith('a'))
print("f3",f3,'\n')


# find all foo and replace with bar and create a backup
#perl -i.BAK -pe 's/foo/bar/g;' *.txt


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

firsts = (p[0] for p in people)
print(firsts)

names = (f"{p[0]} {p[1]}" for p in people)
print(names)
names = (f"{p[0]} {p[1]}" for p in people if p[1] > 'E')
print(names)


#THIS LOOKS VERY USEFUL
names = (f"{p[0]} {p[1]}" for p in people if p[1][0] > 'E')

print(names)
# can loop over generators
for name in names:
    print(name, end=' ')
print('\n\n')
print("-"*60)
print(names)
for name in names:
    print("a:",name, end=' ')
