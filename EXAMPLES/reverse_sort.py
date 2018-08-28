#!/usr/bin/env python

fruit = ["pomegranate", "cherry", "apricot", "date", "Apple",
    "lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
    "papaya", "FIG", "pear", "banana", "Tamarind", "persimmon",
    "elderberry", "peach", "BLUEberry", "lychee", "grape" ]


print("reverse, case-sensitive:")
fsort = sorted(fruit, reverse=True)   # <1>
print(" ".join(fsort))
print()

print("reverse, case-insensitive:")
fsort = sorted(fruit, reverse=True, key=lambda e: e.lower())  # <2>
print(" ".join(fsort))
print()
