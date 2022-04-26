#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10

if (number < 0):
    number = number * -1
    last_digit = number % 10
    last_digit = last_digit * -1
    number = number * -1

if (last_digit < 6 and last_digit != 0):
    return(f"Last digit of {number} is {last_digit} and is less than 6 or 0")
elif (last_digit > 5):
    return(f"Last digit of {number} is {last_digit} and is greater that 5")
elif (last_digit == 0):
    return(f"Last digit of {number} is {last_digit} and is 0")
