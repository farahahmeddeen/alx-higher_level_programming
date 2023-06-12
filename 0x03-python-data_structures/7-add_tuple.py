#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = len(tuple_a)
    b = len(tuple_b)
    value_a = tuple_a[0] if a >= 1 else 0
    value_b = tuple_b[0] if b >= 1 else 0
    sum_1 = value_a + value_b
    value_a = tuple_a[1] if a >= 2 else 0
    value_b = tuple_b[1] if b >= 2 else 0
    sum_2 = value_a + value_b
    new_tuple = (sum_1, sum_2)
    return (new_tuple)
