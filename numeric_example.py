#!/usr/bin/env python
#integer
i1 = 100
i2 = 0x100
i3 = 0b100
i4 = 0o100
#floats
f1= 1234312.12
f2= .34
f3= 1.23e18


#integers can be as big as necessary

x=22
y=5

print(x + y)
print(x * y)
print(x - y)
print(x / y)
print(x // y)
print(x ** y)

print(x % y)


a=5
b=0
try:
    result = a/b
except ZeroDivisionError as err:
    print(err)
else:
    print(result)

i=20
i*= 2 # i=i*2
print(i)

a = "DeadBeef"
i = int(a,16)
print(i*10)
print(a*10)
print("-"* 60)
c = 10
print(a, b, c)
print(a)
print(a, end='')
print(b)
print(a,b,c,sep='/')
print(c,a,b,sep=',',flush=True)


m = 23.614654646
print(f"{m:.2f}")


x=23.454
print(f"{m:b}")