#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    s = len(my_list)
    if idx < 0 or idx > s:
        return (my_list)
    new = list(my_list)
    new[idx] = element
    return (new)

