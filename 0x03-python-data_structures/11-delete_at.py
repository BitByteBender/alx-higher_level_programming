#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    copiedStr = []
    if (idx < 0 or idx > (len(my_list) - 1)):
        return (my_list)
    else:
        for i in range(0, len(my_list)):
            if (i == idx):
                continue
            copiedStr.append(my_list[i])
    return (copiedStr)
