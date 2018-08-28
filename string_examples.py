#!/usr/bin/env python
"""
COMMENTS - Documentation String
"""

s1 = "spam\n"
s2 = 'spam\n'
s3 ="""spam\n"""
s4 ='''spam\n'''
s5= r"spam\n"
x=5
s6 = f"Ive got {x} problems"


print(s4)
print(s5)
print(s6)
print("It's a trap!")
print("The 'rose' garden")

print('''the 'rose' "garden" ''')

y=6

print("I have {} problems but {} answers".format(x,y))

#supports unicode
degrees = "\u00b0"
print("it will be 90\u00B0 in albany this week")

print(f"it will be 90{degrees} in albany this week")