import sys
from tempconv import c2f, f2c

usrtemp = sys.argv[1]
scale_in = sys.argv[2]

#usrtemp = input("Enter a Temperature Value in # <UNIT>:")
if sys.argv[2] == 'F' or sys.argv[2] == 'f':
    try:
        usrtemp = float(usrtemp)
        temp = f2c(usrtemp)
        print(f"Temperature in Celsius is: {temp:.2f}")
    except Exception as err:
        print("Value not a Number:", err, f"Error Name:{type(err).__name__}")
elif sys.argv[2] == 'C' or sys.argv[2] == 'c':
    try:
        usrtemp = float(usrtemp)
        temp = c2f(usrtemp)
        print(f"Temperature in Fahrenheit is: {temp:.2f}")
    except Exception as err:
        print("Value not a Number:", err, f"Error Name:{type(err).__name__}")
else:
    print("YOU ENTERED A SCALE NOT ACCEPTED")