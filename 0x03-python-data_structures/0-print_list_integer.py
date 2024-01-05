#!/usr/bin/python3

i = 0


def print_list_integer(my_list=[]):
    global i
    if (i < len(my_list)):
        print("{}".format(my_list[i]))
        i += 1
        print_list_integer(my_list)
