#!/usr/bin/env python

# while EXPR:
#    ...

while True:
    user_input = input("What is your name?")
    if user_input == 'q':
        break
    if user_input == '':
        continue
    print("Why good morning, {}".format(user_input))

print("after break")
