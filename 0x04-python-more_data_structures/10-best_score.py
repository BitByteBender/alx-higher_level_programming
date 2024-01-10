#!/usr/bin/python3

def best_score(a_dictionary):
    key_store = ""
    if not a_dictionary:
        return (None)
    else:
        key_store = max(a_dictionary, key=a_dictionary.get)
    return (key_store)
