#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    copydir = a_dictionary.copy()
    for key in copydir:
        element = copydir.get(key)
        if element == value:
            del a_dictionary[key]
    return a_dictionary
