#!/usr/bin/env python3
def print_last_digit(number):
    if number < 10:
        return number
    else:
        ans = number % 10
        return ans
