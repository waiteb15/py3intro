#!/usr/bin/env python

# get C temp from cmd line
# convert temp to float
# convert float value to F
# print results
import sys

raw_c_temp = float(sys.argv[1])
c_temp = float(raw_c_temp)
f_temp = ((9 * c_temp) / 5) + 32
print("{}\u00B0C is {}\u00B0F".format(c_temp, f_temp))


