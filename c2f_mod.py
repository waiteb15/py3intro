
from tempconv import c2f
usrtemp = input("Enter a Temperature Value in Celsius:")
try:
    fahrenheit_temp = c2f(float(usrtemp))
    print(f"Temperature in Fahrenheit is: {fahrenheit_temp:.2f}")
except Exception as err:
    print("Value not a Number:",err,type(err).__name__)



