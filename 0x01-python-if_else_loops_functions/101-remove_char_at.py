#!/usr/bin/python3

def remove_char_at(str, n):
    copiedStr = ""
    for i in range(len(str)):
        if not (i == n):
            copiedStr += str[i]
    return (copiedStr)
