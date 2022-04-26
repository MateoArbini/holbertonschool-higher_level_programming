#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
tot = number
last_digit = number % 10

if (tot < 0):
    tot = tot * -1
    last_digit = tot % 10
    last_digit = last_digit * -1
    tot = tot * -1

if (last_digit < 6 and last_digit != 0):
    print(f"Last digit of {tot} is {last_digit} and is less than 6 or 0")
elif (last_digit > 5):
    print(f"Last digit of {tot} is {last_digit} and is greater that 5")
elif (last_digit == 0):
    print(f"Last digit of {tot} is {last_digit} and is 0")
