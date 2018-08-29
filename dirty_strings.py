#!/usr/bin/python3

def cleanup(stringval):
    y = stringval.strip().lower()
    return y

spam = [ 
    "Spam", 
    "eggs  ",
    "   spam    ",
    "     spam spam     ", 
    "SPAM	", 
    "       SPAM and eggs    ",
    "Spam",
    "   Spam,    spam, spam,    spam, spam, eggs, and spam      ",
]

for j, i in enumerate(spam):
    print("before:", i)
    i = cleanup(i)
    print("after:", i)
    spam[j] = i


print(spam)