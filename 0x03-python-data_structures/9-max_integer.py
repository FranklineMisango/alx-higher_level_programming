#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        a = sorted(my_list, reverse=True)

        return a[0]
