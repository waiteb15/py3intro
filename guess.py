#!/usr/bin/env python
# ask uer for a numebr
#Loop over while true
#Create a guess from initialied max valu




max_val = 26
min_val = 0

print('Think of a number between 1 and 25:')


while True:
    guess = ((max_val + min_val)) // 2
    usr_check = input(f"Is {guess} your number? Enter 'y' for yes, 'h' for too high, and 'l' for too low!(q for quit)")
    if usr_check == 'y':
        print("Yay I got your number!")
        break
    elif usr_check == 'l':
        print("Oops I'm too low")
        min_val = guess
        continue
    elif usr_check == 'h':
        print("whoops, too high")
        max_val = guess
        continue
    elif usr_check == 'q':
        break
    else:
        print("Enter 'y' (I got it!), 'l' (too low), 'h'(too high) or 'q' to quit!")
        continue
