#!/usr/bin/python3

def no_c(my_string):
    copiedStr = ""
    for i in range(0, len(my_string)):
        if not (my_string[i] == 'C' or my_string[i] == 'c'):
            copiedStr += my_string[i]
    return (copiedStr)
