#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    s = len(my_list)
    if idx < s and idx >= 0:
        my_list[idx] = element
        return (my_list)
