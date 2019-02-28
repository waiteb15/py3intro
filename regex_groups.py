#!/usr/bin/env python

import re

text = "Event at 10:42 AM"

pattern = r"(\d{2}):(\d{2})\s+[AP]M"

m = re.search(pattern, text)
if m:
    print(m.group(0))
    print(m.group(1))
    print(m.group(2))
    print(m.groups())

pattern = '[a-z]{5,}'

text = 'abc  abc hah ytr xx humerus wombat foo peril'
text2 = text

m = re.search(pattern, text)
if m:
    print(m.group(0))   # m.group(0)
all_words = re.findall(pattern, text)
print("all_words:", all_words)
for word in all_words:
    replacement = f"**{word}**"
    text = re.sub(word, replacement, text)
print(text)

def doit(m):
    return f"**{m.group(0)}**"

t = re.sub(pattern, doit, text2)
print(t)
