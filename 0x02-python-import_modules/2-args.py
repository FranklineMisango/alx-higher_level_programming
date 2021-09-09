#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv)
    if args == 1:
        print("{} arguments.".format(args - 1))
    else:
        print("{} arguments:".format(args - 1))
    x = 1
    for arg in sys.argv[1:]:
        print("{}: {}".format(x, arg))
        x += 1
