#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    cmpt = 0
    for index in range(x):
        try:
            print("{:d}".format(my_list[index]), end='')
            cmpt += 1
        except (ValueError, TypeError):
            continue

    print('')
    return cmpt
