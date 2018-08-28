#!/usr/bin/env python
# ask uer for a numebr
#Loop over while true
#Create a guess from initialied max valu

import sys

min_val = 0
max_val = sys.argv[1]


i = 1

if max_val.isalpha() == False:
    max_val = float(max_val)
    print(f'Think of a number between 1 and {max_val} please!')
    while True:
        guess = ((max_val + min_val)) // 2
        usr_check = input(f"Is {guess} your number? Enter 'y' for yes, 'h' for too high, and 'l' for too low!(q for quit)")
        if usr_check == 'y':
            if i == 1:
                print(f"Yay I got your number in {i} guess!")
            else:
                print(f"Yay I got your number in {i} guesses!")
            break
        elif usr_check == 'l':
            print("Oops I'm too low")
            min_val = guess
            i += 1
            continue
        elif usr_check == 'h':
            print("whoops, too high")
            max_val = guess
            i += 1
            continue
        elif usr_check == 'q':
            break
        else:
            print("Enter 'y' (I got it!), 'l' (too low), 'h'(too high) or 'q' to quit!")
            continue
else:
    print("You Broke it because you didn't enter a number")