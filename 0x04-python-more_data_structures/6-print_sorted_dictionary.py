#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for fh in sorted(a_dictionary):
        print("{:s}: {}".format(fh, a_dictionary[fh]))
