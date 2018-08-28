#!/usr/bin/env python

while True:
   usrtemp = input("Enter a Temperature Value in Celsius:(or q for quit)")
   if usrtemp == 'q':
       break
   elif usrtemp.isalpha() == False:
       usrtemp = float(usrtemp)
       fahrenheit_temp = ((9 * usrtemp) / 5) + 32
       print(f"Temperature in Fahrenheit is: {fahrenheit_temp:.2f}")
   else:
       print('Enter a Number!')
       continue




