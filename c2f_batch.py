import sys

usrtemp = sys.argv[1]

#usrtemp = input("Enter a Temperature Value in Celsius:")

if usrtemp.isalpha() == False:
    usrtemp = float(usrtemp)
    fahrenheit_temp = ((9 * usrtemp) / 5) + 32
    print(f"Temperature in Fahrenheit is: {fahrenheit_temp:.2f}")
else:
    print('enter a number!!!!')


