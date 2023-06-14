#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    l_keys = list(new.keys())
    for fh in l_keys:
        new[fh] *= 2
    return (new)
