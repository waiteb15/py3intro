#!/usr/bin/env python

def add(arg1, arg2 ):
    val = float(arg1) + float(arg2)
    return val

def subtract(arg1, arg2 ):
    val = float(arg1) - float(arg2)
    return val

def divide(arg1, arg2):
    if float(arg2) == 0:
        print("Cannot Divide by Zero")
        return
    else:
        val = float(arg1) / float(arg2)
        return val

def multiply(arg1, arg2 ):
    val = float(arg1) * float(arg2)
    return val

def exponent(arg1, arg2 ):
    val = float(arg1) ** float(arg2)
    return val


while True:
    user_value = input("Enter a math expression( ex. '9 + 4' make sure you seperate by whitespace)(q for quit):")
    if user_value == 'q' or user_value == 'Q':
        break
    else:
        values = user_value.split(' ')
        if values[1] == '+':
            result = add(values[0],values[2])
        elif values[1] == '-':
            result = subtract(values[0],values[2])
        elif values[1] == '*':
            result = multiply(values[0],values[2])
        elif values[1] == '/':
            result = divide(values[0], values[2])
        elif values[1] == '**':
            result = exponent(values[0], values[2])
        else:
            print("you didnt follow directions so I quit")
            break
        print(f"Your answer is {result}")

