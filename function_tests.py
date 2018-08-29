#!/usr/bin/env python
def c2f():
    pass


def get_message():
    return "HELLO, NY"

def display_greeting():
    message = get_message()
    print(message)

m = get_message()
print(m)
display_greeting()

def null():
    pass

x = null()

print(x)

def hello(whom):
    print("Hello,",whom)

hello('world')
hello(10)
hello(['a','b','c'])

def spam(a,b):
    pass

#*z is optional parameters
#a, b are required named parameters
#**c optional named parameters
def blurf(x, y, *z, a, b, **c):
    print(x,y,z,a, b,c )
    pass

blurf(1,2,a=3,b=4)

blurf(1,2,3,4,6,7,8, a=7, c=9,f=10,b=10)

def blag(*,filename, tkv):
    pass
blag(filename='fred.txt',tkv=10.0)

def josh(x,y,z=None):
    print(x,y,z)

josh(1,2)
josh(1,2,3)