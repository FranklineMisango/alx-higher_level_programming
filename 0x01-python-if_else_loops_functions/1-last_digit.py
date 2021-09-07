#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10

if last_digit == 0:
    ending = "and is 0"
elif last_digit < 6:
    ending = "and is less than 6 and not 0"
else:
    ending = "and is greater than 5"

print("Last digit of {} is {} {}".format(number, last_digit, ending))
