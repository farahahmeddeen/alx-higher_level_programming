#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    n_list = []
    for f in range(0, list_length):
        try:
            div = (my_list_1[f] / my_list_2[f])
        except TypeError:
            div = 0
            print("wrong type")
        except ZeroDivisionError:
            div = 0
            print("division by 0")
        except IndexError:
            div = 0
            print("out of range")
        finally:
            n_list.append(div)
    return n_list
