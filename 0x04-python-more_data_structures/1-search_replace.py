#!/usr/bin/python3


def search_replace(my_list, search, replace):
    newList = my_list.copy()
    if not my_list:
        return (None)
    else:
        for i in range(len(my_list)):
            if (newList[i] == search):
                newList[i] = replace
    return (newList)