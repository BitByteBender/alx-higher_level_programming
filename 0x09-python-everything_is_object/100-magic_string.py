#!/usr/bin/python3
def magic_string():
    magic_string.i = magic_string.i + 1 if hasattr(magic_string, 'i') else 1
    return (', '.join(["BestSchool"] * magic_string.i))
