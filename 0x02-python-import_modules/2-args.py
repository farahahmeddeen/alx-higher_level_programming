#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    fh = len(argv) - 1
    if fh == 0:
        print("0 arguments.")
    elif fh == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(fh))
    for j in range(1, fh + 1):
        print("{}: {}".format(j, argv[j]))

