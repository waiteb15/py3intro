usrtemp = input("Enter a Temperature Value in Celsius:")

try:
    usrtemp = float(usrtemp)
    fahrenheit_temp = ((9* usrtemp) /  5) + 32
    print(f"Temperature in Fahrenheit is: {fahrenheit_temp:.2f}")
except Exception as err:
    print("Value not a Number:",err,type(err).__name__)





