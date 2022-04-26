#!/usr/bin/python3
def print_last_digit(number):
    ln = 0
    if (number > 0):
        ln = number % 10
        print(ln, end='')
    elif (number < 0):
        number = number * -1
        number = number % 10
        ln = number
        print(ln, end='')
    else:
        ln = 0
        print(ln, end='') 
    return(ln)
