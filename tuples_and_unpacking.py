#!/usr/bin/env python

person = "Tom", "Hanks", 56

print(len(person))
print(person[0], person[1])

#  var1, var2, ....  = ITERABLE

first_name, last_name, age = person

human = person

print(human[2])

# VERBOTEN:
# human[0] = "you cannot pass"
# person[0] = "nope"
print()

stuff = ['bike', 'car', 'rabbit', 'wombat', 'torch']
a, b, *c = stuff
print(a, b, c, '\n')

a, *b, c = stuff
print(a, b, c, '\n')

*a, b  = stuff
print(a, b, '\n')

x = [5, 10]
x = 5, 10
x = list(x)
x = tuple(x)

print(x, y)

x, y = y, x
print(x, y)



