#!/usr/bin/python3

i = 0


def print_reversed_list_integer(my_list=[]):
    global i
    if (i < len(my_list)):
        print("{}".format(my_list[len(my_list) - i - 1]))
        i += 1
        print_reversed_list_integer(my_list)
