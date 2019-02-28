#!/usr/bin/env python
import re
import sys

pattern = r"[^a-z']+"

counts = {}

for file_name in sys.argv[1:]:
    with open(file_name) as file_in:
        text = file_in.read()
        all_words = re.split(pattern, text.lower())
        # print(all_words)
        for word in all_words:
            if word not in counts:
                counts[word] = 0
            counts[word] = counts[word] + 1

for word, count in sorted(counts.items(), key=lambda e:(e[1], e[0])):
    print(word, count)
