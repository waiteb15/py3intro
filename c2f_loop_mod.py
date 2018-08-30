#!/usr/bin/env python
from tempconv import c2f

while True:
   usrtemp = input("Enter a Temperature Value in Celsius:(or q for quit)")
   if usrtemp == 'q':
       break
   elif usrtemp.isalpha() == False:
       usrtemp = float(usrtemp)
       fahrenheit_temp = c2f(usrtemp)
       print(f"Temperature in Fahrenheit is: {fahrenheit_temp:.2f}")
   else:
       print('Enter a Number!')
       continue




