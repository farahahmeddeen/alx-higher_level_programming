#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for fh in range(0, x):
            print(my_list[fh], end="")
            count = count + 1
    except IndexError:
        None
    print()
    return (count)
