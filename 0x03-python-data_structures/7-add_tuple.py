#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    result = ()
    for i in range(max(len(tuple_a), len(tuple_b))):
        newTuple_a = tuple_a[i] if (len(tuple_a) > i) else 0
        newTuple_b = tuple_b[i] if (len(tuple_b) > i) else 0
        result += (newTuple_a + newTuple_b, )
    return (result)
