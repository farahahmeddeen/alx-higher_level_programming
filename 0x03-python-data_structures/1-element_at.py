#!/usr/bin/python3
def element_at(my_list, idx):
    s = len(my_list)
    if (idx > s - 1 or idx > 0):
        return (None)
    return (my_list[idx])
