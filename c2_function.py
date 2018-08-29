
def c2f_func(usrtemp):
    usrtemp = float(usrtemp)
    fahrenheit_temp = ((9* usrtemp) /  5) + 32
    return fahrenheit_temp


usrtemp = input("Enter a Temperature Value in Celsius:")
new_temp = c2f_func(usrtemp)
print(f"{usrtemp} in Celsisus in  Fahrenheit is: {new_temp:.2f}")
