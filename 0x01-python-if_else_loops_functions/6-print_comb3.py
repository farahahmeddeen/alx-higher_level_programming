#!/usr/bin/python3
for j in range(8):
    for h in range(j + 1, 10):
        print("{:d}{:d}, ".format(j, h), end="")
print("{:d}".format(89))
