#!/usr/bin/python3

i = 0


def print_reversed_list_integer(my_list=[]):
    global i
    if not my_list:
        return
    elif (i < len(my_list)):
        print("{:d}".format(my_list[len(my_list) - i - 1]))
        i += 1
        print_reversed_list_integer(my_list)
