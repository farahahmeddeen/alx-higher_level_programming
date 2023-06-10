#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for sh in my_string:
        if sh != "c" and sh != "C":
            new_string = new_string + sh
    return (new_string)
