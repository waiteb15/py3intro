#!/usr/bin/env python

from struct import Struct

values = 7, 6, 42.3, b'Guido'

demo = Struct('iif10s')

print("Size of data: {} bytes".format(demo.size))

binary_stream = demo.pack(*values)

int1, int2, float1, str1 = demo.unpack(binary_stream)
str1 = str1.decode().rstrip('\x00')

print(int1, int2, float1, str1)
