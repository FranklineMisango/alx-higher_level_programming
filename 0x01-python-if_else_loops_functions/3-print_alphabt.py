#!/usr/bin/python3
def lowercaseAlphabets():
   for i in 'abcdefghijklmnopqrstuvwxyz':
    if (i != "q" and i != "e"):
        print("{}".format(i), end="")
lowercaseAlphabets()
