#!/usr/bin/python3
def uppercase(str):
    for j in range(len(str)):
        h = ord(str)
        if h >= 97 and h <= 122:
            h = h - 32
            print("{:c}".format(h), end="")
print()
