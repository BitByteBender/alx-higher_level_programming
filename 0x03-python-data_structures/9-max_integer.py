#!/usr/bin/python3

i = 0


def getMax(my_list, max):
    if not my_list:
        return (None)

    global i
    if (i == len(my_list)):
        return (max)
    else:
        if (my_list[i] > max):
            max = my_list[i]
        i += 1
        return getMax(my_list, max)


def max_integer(my_list=[]):
    return (getMax(my_list, 0))
