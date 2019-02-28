#!/usr/bin/env python

# def c2f():
#     # do conversion
#     print("f is", f)
def main():
    display_greeting()
    hello('Mom')
    hello('world')
    hello(3)
    hello(123.45)
    hello(['a','b','c'])

def get_message():
    return "Hello, KAPL world"

def display_greeting():
    message = get_message()
    print(message)

m = get_message()

display_greeting()

def null():
    pass

x = null()

def hello(whom: str):
    print("Hello,", whom)



def spam(a, b):
    pass


def blurf(x, y, *z, a, b, **c):
    print("x:", x)
    print("y:", y)
    print("z:", z)
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print('=' * 10)

blurf(1,2,a=3,b=4)
blurf(1, 2, 3, 4, 5, 6, d=7, c=9, b=10, a=12)

def _blag(*, filename, tkv):
    pass

_blag(filename='fred.txt', tkv=4.6)



def josh(x, y, z=None):
    if z is not None:
        pass

    print(x, y, z)


josh(1, 2)
josh(1, 2, 3)


def whatever(x, y, z):
    pass # do whatever...


if __name__ == '__main__': # if script not module
    main()











