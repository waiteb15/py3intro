#!/usr/bin/env python
import re
import sys

all_words={}
file_name = sys.argv[1]

rx_wordsep = re.compile(r"[^\w']+",re.I)

with open(file_name) as file_in:
    words = rx_wordsep.split(file_in.read())
    for word in words:
        if word == '' or word == "'":
            continue
        all_words[word.lower()] = all_words.get(word.lower(),0) + 1


for word, count in sorted(all_words.items()):
    print(f"{word}:{count}")


