#!/usr/bin/env python
# SCOPES
# local  nonlocal  global builtin
import sys
x = 100

def print(*args, **kwargs):
    sys.stdout.write("HAHA\n")
#     for arg in args:
#         sys.stdout.write(str(arg) + ' ')
#     sys.stdout.write('\n')

def spam():
    x =2
    y=25

    def ham():
        print("In ham():y is ", y)
    print("in spam: x=", x)
    print("in spam: x=", y)
    return ham

h = spam()
h()

print(x)

# print("in main: y =", y)
