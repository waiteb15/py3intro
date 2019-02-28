#!/usr/bin/env python

value = 51

if value > 75:
    print("wombat")
    print('wallaby')
elif value > 50:
    print("kookaburra")
elif value > 25:
    print("platypus")
elif 10 < value <= 25:
    print("blue-ringed octopus")
else:
    print("kangaroo")

# 0  or len(x) == 0

def a():
    print("a")
    return 0
def b():
    print("b")
    return 2

def c():
    print("c")
    return 3

def d():
    print("d")
    return 4

print(a() and b() and c() and d())

