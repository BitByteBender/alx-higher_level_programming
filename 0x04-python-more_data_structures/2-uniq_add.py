#!/usr/bin/python3


def uniq_add(my_list=[]):
    sum = 0
    for i in range(len(my_list)):
        isUniq = True
        for j in range(0, i):
            if (my_list[i] == my_list[j]):
                isUniq = False
                break
        if (isUniq):
            sum += my_list[i]
    return (sum)
