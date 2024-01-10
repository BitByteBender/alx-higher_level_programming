#!/usr/bin/python3


def weight_average(my_list=[]):
    sum_1 = 0
    sum_2 = 0
    average = 0
    if not my_list:
        return (0)
    else:
        for i in range(len(my_list)):
            sum_1 += my_list[i][0] * my_list[i][1]
            sum_2 += my_list[i][1]
    average = sum_1 / sum_2
    return (average)
