#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    else:
        if idx > len(my_list):
            return my_list
        else:
            temp_list = my_list.copy()
            temp_list[idx] = element
            return temp_list
