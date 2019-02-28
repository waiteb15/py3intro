#!/usr/bin/env python

list1 = list()  # new, empty, list
list2 = ['red', 'white', 'rose']
tuple1 = 'red', 'white', 'rose'
set1 = {'red', 'white', 'rose'}

list3 = []
# mylist = list(......)
list4 = "NC:NJ:WI:NY:WA:TX:CA".split(':')

x=2+5
x = 2 + 5

colors = ['red', 'amber',     'cream', 'blue', 'white',
          'orange',     'chartreuse']

print(colors, '\n')
print(colors[0], colors[3])
colors.append('pink')
print(colors, '\n')
more_colors = ['navy', 'parakeet', 'yellow']

colors.extend(more_colors)

print(colors, '\n')

colors.insert(0, 'scarlet')
colors.insert(5, 'black')
print(colors, '\n')

del colors[3]  # remove the 4th element
print(colors, '\n')

c = colors.pop()
print(c)
print(colors, '\n')

c = colors.pop(2)
print(c)
print(colors, '\n')

colors.remove('chartreuse')
print(colors, '\n')

print(colors[0], colors[6], '\n')
print(colors[-1], '\n')
print(colors[len(colors)-1], '\n')
print(colors[len(colors)-10], '\n')

#  L[START:STOP]  L[START:STOP:STEP]  L[:STOP]  L[START:]  L[::]
print(colors[0:5], '\n')
print(colors[:5], '\n')
print(colors[5:], '\n')
print(colors[3:8], '\n')
print(colors[::], '\n')

a = "Bob"
b = a
a = "Fred"
print(a, b)

names = ['Manny', 'Moe']
pep_boys = names  # pep_boys and names are both bound to the list object
pep_boys.append('Jack')
print(names)
stooges = names[::]  # list(names)
stooges.append('Shemp')
print(names, pep_boys, stooges)

print(colors)
even_more_colors = ['cyan', 'magenta', 'burgundy']
colors[3:3] = even_more_colors
print(colors, '\n')

print(colors[::2])
print(colors[::3])

movie_star = 'William Powell'
print('>' + movie_star[:8] + '<')
print(movie_star[8:11])
print(movie_star[-6:], '\n')

print(colors, '\n')

# for VAR,... in ITERABLE:
#    ...
for wombat in colors:   #  for @colors { print; }
    print(wombat)

print(wombat)

# while True:
#     try:
#         wombat = next(colors)
#     except StopIteration:
#         break

print('-' * 60)
for color in colors[3:-1]:
    print(color)

print('-' * 60)
# for i, color in enumerate(colors):
#     if 3 < i < len(colors) - 1:
#         print(color)
print(list(enumerate(colors)))
