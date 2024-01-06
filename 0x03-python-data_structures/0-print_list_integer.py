#!/usr/bin/python3

def print_list_integer(my_list=[]):

    if (i < len(my_list)):
        print("{}".format(my_list[i]))
        i += 1
        print_list_integer(my_list)
