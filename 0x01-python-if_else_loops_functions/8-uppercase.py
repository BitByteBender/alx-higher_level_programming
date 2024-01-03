#!/usr/bin/python3

def uppercase(str):
    copiedStr = ""
    for alphabet in str:
        if (97 <= ord(alphabet) <= 122):
            copiedStr += chr(ord(alphabet) - 32)
        else:
            copiedStr += alphabet
    print(copiedStr)
