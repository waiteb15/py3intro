#!/usr/bin/env python
from collections import Counter

counts = {}

with open('DATA/breakfast.txt') as breakfast_in:
    for line in breakfast_in:
        item = line.rstrip()
        if item not in counts:
            counts[item] = 0

        counts[item] = counts[item] + 1

print(counts)

with open('DATA/breakfast.txt') as breakfast_in:
    foods = [b.rstrip() for b in breakfast_in]
    counts = Counter(foods)

print(counts)

with open('DATA/words.txt') as words_in:
    letters = [w.rstrip()[0] for w in words_in]
    letter_counts = Counter(letters)

print(letter_counts.most_common(3))
print(letter_counts['x'])
print(letter_counts)
