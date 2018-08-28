#!/usr/bin/env python
import sys

if len(sys.argv) == 2:
    high_limit = int(sys.argv[1])
else:
    high_limit = 50
    print("High Limit Set to 50!")

is_prime = [1] * (high_limit+1)

for num in range(2,high_limit+1):
    if is_prime[num]:
        print(num)
        for m in range(num, high_limit+1, num):
           is_prime[m] = 0

