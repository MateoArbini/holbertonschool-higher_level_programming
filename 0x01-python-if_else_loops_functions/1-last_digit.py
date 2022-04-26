#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
ln = number

if (ln < 0):
    ln = ln * -1
    last_digit = ln % 10
    last_digit = last_digit * -1
    ln = ln * -1

if (last_digit < 6 and last_digit != 0):
    print(f"Last digit of {ln} is {last_digit} and is less than 6 and not 0")
elif (last_digit > 5):
    print(f"Last digit of {ln} is {last_digit} and is greater than 5")
else:
    print(f"Last digit of {ln} is {last_digit} and is 0")
