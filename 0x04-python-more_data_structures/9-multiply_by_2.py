#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    final = {}
    for key in a_dictionary:
        element = a_dictionary.get(key)
        value = element * 2
        final.update({key: value})
    return final
