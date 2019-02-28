#!/usr/bin/env python
"""
String examples for my excellent students
"""


s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r"spam\n"
x = 5
s6 = f"I've got {x} problems"


print(s4)
print(s5)
print(s6)
print("It's a trap!")
print("The 'rose' garden")


print('''The 'rose' "garden"''')


# legacy formatting
x = 5
print("I have %s problems" % (x))

# modern
print("I have {} problems".format(x))

# f-strings VERY modern (hotness)
print(f"I have {x} problems")

get_customers_from_omaha = """
select *
from customers
where city = "Omaha"
"""

degrees = "\u00B0"
print(f"It will be 90{degrees} in Albany this week")










