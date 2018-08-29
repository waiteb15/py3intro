#!/usr/bin/env python

count = 0
with open('DATA/alice.txt') as alice_in:
    if __name__ == '__main__':
        for raw_line in alice_in:
            if 'Alice' in raw_line:
                count += 1


print(f"There are {count} lines with the word Alice in them")