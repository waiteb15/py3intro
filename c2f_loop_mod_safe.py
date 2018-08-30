#!/usr/bin/env python
from tempconv import c2f, f2c

while True:
   usrtemp = input("Enter a Temperature Value with unit separated by a space:(or q for quit)").split(' ')
   if usrtemp[0] == 'q':
       break
   try:
        temp = float(usrtemp[0])
   except Exception as err:
        print("Value not a Number:", err, f"Error Name:{type(err).__name__}")
        print("enter a number")
   unit = usrtemp[1].lower()
   if unit == 'c':
       temp = float(temp)
       fahrenheit_temp = c2f(temp)
       print(f"Temperature in Fahrenheit is: {fahrenheit_temp:.2f}")
   elif unit == 'f':
       temp = float(temp)
       fahrenheit_temp = f2c(temp)
       print(f"Temperature in Celsius is: {fahrenheit_temp:.2f}")
   else:
       print('Enter F or C')
   continue




