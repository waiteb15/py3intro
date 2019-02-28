#!/usr/bin/env python

# get C temp from user
# convert temp to float
# convert float value to F
# print results

raw_c_temp = input("Enter Celsius temperature: ")
c_temp = float(raw_c_temp)
f_temp = ((9 * c_temp) / 5) + 32
print("{}\u00B0C is {}\u00B0F".format(c_temp, f_temp))


