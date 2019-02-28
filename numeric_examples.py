#!/usr/bin/env python

i1 = 100
i2 = 0x100
i3 = 0b100
i4 = 0o100

f1 = 123.456
f2 = 123.
f3 = .456
f4 = 1.234e17

x = 22
y = 5

print(x + y)
print(x * y)
print(x - y)
print(x / y)
print(x // y)
print(x ** y)
print(x % y)


a = 5
b = 0
try:
    result = a / b
except ZeroDivisionError as err:
    print(err)
else:
    print(result)
print("DONE")


i = 10
i *= 2  # i = i * 2
i /= 5
i **= 5
print(i)



