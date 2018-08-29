#!/usr/bin/env python

d1 = dict()

caps ={'NY' : 'Albany', 'MA': 'Boston', 'ME': 'Augusta'}
d2 = {}
# d1 and d2 do the same thing


daga =[('NY' , 'Albany'), ('MA', 'Boston'), ('ME', 'Augusta')]
d3 = dict(daga)

d4 = dict(NY='Albany', MA='Boston', ME ='Augusta')

staes = ['NY', 'MA', 'ME']
capitals = ['albany', 'boston', 'augusta']
d5 = dict(zip(staes,capitals))

print(d5)

d4['PE'] = 'MADEUP'

print(d4)

for state in 'NY', 'NC','NJ', 'MA':
    print(d4.get(state,"NOT IN LIST"))
print('-'*60)
for capital, state in d4.items():
    print(capital, state)


print(d4.keys())