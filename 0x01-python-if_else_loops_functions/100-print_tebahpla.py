#!/usr/bin/python3

def print_chars(begin, end, move):
    for i in range(begin, end, move):
        char = chr(i + ord('A'))
        if (i % 2 == 1):
            char = char.lower()
        print(char, end='')


print_chars(25, -1, -1)
