#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
total_number = number
last_digit = number % 10

if (total_number < 0):
    total_number = total_number * -1
    last_digit = total_number % 10
    last_digit = last_digit * -1
    total_number = total_number * -1

if (last_digit < 6 and last_digit != 0):
    print (f"Last digit of {total_number} is {last_digit} and is less than 6 or 0")
elif (last_digit > 5):
    print (f"Last digit of {total_number} is {last_digit} and is greater that 5")
elif (last_digit == 0):
    print (f"Last digit of {total_number} is {last_digit} and is 0")
