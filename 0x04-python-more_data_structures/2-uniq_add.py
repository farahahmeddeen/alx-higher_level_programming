#!/usr/bin/python3
def uniq_add(my_list=[]):
    Sum = 0
    uniq_int = set(my_list)
    for j in uniq_int:
        Sum = Sum + j
    return (Sum)
