#!/usr/bin/env python

import re

s = """lorem ipsum M302 dolor sit amet, consectetur r99 adipiscing elit, sed do
 eiusmod tempor incididunt H476 ut labore et dolore magna Q51 aliqua. Ut enim 
ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex  
ea commodo Z883  consequat. Duis aute irure dolor in reprehenderit in  
voluptate velit esse cillum dolore U901 eu fugiat nulla pariatur. 
Excepteur sint occaecat A110 cupidatat non proident, sunt in H332 culpa qui 
officia deserunt Y45 mollit anim id est laborum"""

rx_code = re.compile(r'  [A-Z]   \d{2,3}', re.I | re.X)  # <1>

if rx_code.search(s):  # <2>  # re.search(pattern, text)
                              # rxobj.search(text)
    print("Found pattern.")  
print()

m = rx_code.search(s)
if m:
    print("Found:", m.group())
print()

for m in rx_code.finditer(s):
    print(m.group())
print()

matches = rx_code.findall(s)
print("matches:",  matches)
print()

t = """
blah blah blah
blah blah 
blah
Wombat Tractor Penny Argyle Foo Bar Blah
1      2       3     4      5   6   7
1      2       3     4      5   6   7
1      2       3     4      5   6   7
Gila Monster
blah blah blha blah blah
blah blah
"""

heading = "Wombat Tractor Penny Argyle Foo Bar Blah"

pattern = "Wombat Tractor Penny Argyle Foo Bar Blah\n(.*)\nGila Monster"

m = re.search(pattern, t, re.S)
if m:
    print(m.group(1))
    rows = [[float(n) for n in r.split()] for r in m.group(1).splitlines()]
    print(rows)









