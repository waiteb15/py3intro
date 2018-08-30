#!/usr/bin/env python

import re

s = """lorem ipsum M302 dolor sit amet, consectetur r99 adipiscing elit, sed do
 eiusmod tempor incididunt H476 ut labore et dolore magna Q51 aliqua. Ut enim 
ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex  
ea commodo Z883  consequat. Duis aute irure dolor in reprehenderit in  
voluptate velit esse cillum dolore U901 eu fugiat nulla pariatur. 
Excepteur sint occaecat A110 cupidatat non proident, sunt in H332 culpa qui 
officia deserunt Y45 mollit anim id est laborum"""

rx_code = re.compile(r'[A-Z]\d{2,3}', re.I)  # <1>

if rx_code.search(s):  # <2>
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

# need to add compiles with | functions

rx_code2 = re.compile(r'[A-Z]\d{2,3}', re.I | re.X)  # <1>


t = """
asdfasd
 blah blah
 adfasd
 
wom tractor penny argyle foo bar Blah 
1   2       3     4      5   6   7 
1   2       3     4      5   6   7 


asd
adfasdfa
adfasdf


"""

