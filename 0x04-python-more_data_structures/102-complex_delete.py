#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    l_keys = list(a_dictionary.keys())
    for fh in l_keys:
        if value == a_dictionary.get(fh):
            del a_dictionary[fh]
    return (a_dictionary)
