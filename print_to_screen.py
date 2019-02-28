#!/usr/bin/env python

a = 'fig'
b = 25
c = 14.93923

print(a, b, c)
print()
print(a)
print(a)
print(b)
print(c)

print(a, end='')
print(b, end='')
print(c)
print(a, b, c, sep='/')

m = 23.4567 / 8.2930923
print(m)
print(f"{m:.2f}")
print("{:.2f}".format(m))

bignum = 23942039582039582093582

print(f"{bignum:,d}")

x = 5
print("{:3d}".format(x))
x = 12
print("{:3d}".format(x))
x = 8
print("{:3d}".format(x))

x = 23456489284.2355

print(f"{x:f}")
print(f"{x:e}")

print("{:08b}".format(27))

