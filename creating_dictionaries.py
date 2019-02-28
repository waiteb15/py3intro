#!/usr/bin/env python

d1 = dict()  # new, empty, dict
d2 = {}
data = [('NY','Albany'), ('MA', 'Boston'), ('VT', 'Montpelier'),
        ('NH', 'Concord')]

d3 = dict(data)
d4 = dict(NY='Albany', MA='Boston', VT='Montpelier', NH='Concord')

states = ['NY', 'MA', 'VT', 'NH']
capitals = ['Albany', 'Boston', 'Montpelier', 'Concord']
d5 = dict(zip(states, capitals))

caps = {'NY': 'Albany', 'MA': 'Boston', 'VT': 'Montpelier', 'NH': 'Concord'}

print(d5, '\n')

caps['ME'] = 'Rockport'

for state in 'NY', 'NC', 'NJ', 'ME':
    print(state in caps)
print()

more_caps = {'NC': 'Raleigh', 'NJ': 'Trenton', 'PA': 'Harrisburg',
             'ME': 'Portland'}

caps.update(more_caps)
print(caps)

del caps['NJ']


for state in 'NY', 'NC', 'NJ', 'ME':
    print(caps.get(state, state + ' is not a state'))
print()

print(caps.setdefault('NJ', 'Trenton'))

print(caps, '\n')

print(len(caps))

for capital, state in caps.items():  # similar to enumerate()
    print(capital, state)

print(caps.items())

for c in caps.items():
    print(c)

print(caps.keys())
print(caps.values())
