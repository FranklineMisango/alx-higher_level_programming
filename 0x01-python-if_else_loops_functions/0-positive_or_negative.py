#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number < 0:
    sign = "negative"
elif number == 0:
    sign = "zero"
else:
    sign = "positive"
print("{} is {}".format(number, sign))
