#!/usr/bin/env python

from collections import Counter

with open("DATA/words.txt") as words_in:
    letters = [w.rstrip()[0] for w in words_in]
    letter_counts = Counter(letters)



print(letter_counts.most_common(5))

