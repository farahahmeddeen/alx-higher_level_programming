#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for jj in matrix:
        s = len(jj)
        for h, w in enumerate(jj):
            if (h < s - 1):
                print("{:d} ".format(w), end="")
            else:
                print("{:d}".format(w), end="")
        print("")
