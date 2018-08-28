#!/usr/bin/env python
list1 = list() #new empy list
list2 = ['red', 'white', 'rose']
list3 = []
tuple1 = 'red', 'white', 'rose'
set1 = {'red', 'white', 'rose'}
# mylist = list(.....) # iterable can be passed into this  (some kind of data set)
list4 = "NC:NJ:WI:NY:WA:TX:CA".split(":")
colors = ['red', 'white', 'cream','blue','white'
          , 'orange', 'black']
print(colors)
colors.append('pink')
more_colors = ['green','crayon']
# this shoes the difference between append and extend
#colors.append(more_colors)
print(colors)
colors.extend(more_colors)
print(colors)
colors.insert(0, "scarlet")
colors.insert(5,"yellow")
print(colors,'\n')
del colors[3] #remove the 4th element
print(colors,'\n')
# set c to taht value and delete it
# c=colors.pop()
# print(c)
# print(colors,"\n")
colors.remove('yellow')
print(colors)
# negative indices start counting at the end
print(colors[1])
#print(colors[-8])
#
print(colors[0:5])
print(len(colors))
print(colors[::],'\n')
even_more_colors = ['cyan', 'magenta', 'burgundy']
colors[3:3] = even_more_colors
print(colors)
#when you assign to a slice, things are added individually
colors[3:4] = even_more_colors
print(colors)
# names = ["jack","johan"]
# names2 = names
# names2.append("brian")
# print('names:',names)
# #names2 and names are just a name for the same list
# #instead do this:
# stooges = names[::]
# stooges.append('danny')
# print('names:',names)
# print('stooges:',stooges)
movie_star = 'William Powell'

print(movie_star[:7])
print(movie_star[8:11])
print(movie_star[8::2])

print(colors,'\n')
#for VAR in Iterable
# list, tuple, string, set, dictionary

for dummy in colors:
    print(dummy + ' a aa')

print(dummy)