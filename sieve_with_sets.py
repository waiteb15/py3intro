#!/usr/bin/env python
import sys

if len(sys.argv) == 2:
    high_limit = int(sys.argv[1])
else:
    high_limit = 50
    print("High Limit Set to 50!")

#is_prime = [1] * (high_limit+1)
prime_nums = set()
print(2)
for num in range(3,high_limit+1):
    if num not in prime_nums:
        print (num)
        for m in range(num, high_limit+1, num):
           prime_nums.add(m)

