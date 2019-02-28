#!/usr/bin/env python


d1 = {'a': 5, 'b': 10, 'c': 15}
d2 = {'a': 'wombat', 'b': 'wallaby', 'c': 'koala'}

d3 = { x: (d1[x], d2[x]) for x in d1}
d4 = { x: (y, d2[x]) for x, y in d1.items()}

print(d3, '\n')
print(d4, '\n')

d5 = dict(zip(d1.keys(),zip(d1.values(), d2.values())))
print(d5)
