#!/usr/bin/env python
# local   nonlocal global builtin
import sys
x = 100

def print(*args, **kwargs):
    sys.stdout.write("HA HA HA\n")
    # for arg in args:
    #     sys.stdout.write(str(arg) + ' ')
    # sys.stdout.write('\n')

def spam():
    x = 2
    y = 25

    def ham():
        print("In ham(): y is", y)

    print("in spam(): x =", x)
    print("in spam(): y =", y)
    return ham

h = spam()
h()
print("main: x is", x)
