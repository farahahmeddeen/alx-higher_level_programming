#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    total = 0
    fh = len(argv) - 1
    for j in range(j, fh + 1):
        total += int(argv[j])
    print(total)
