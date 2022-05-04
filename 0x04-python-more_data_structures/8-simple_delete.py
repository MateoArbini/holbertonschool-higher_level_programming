#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for keys in a_dictionary:
        if keys == key:
            del a_dictionary[keys]
            return a_dictionary
    return a_dictionary
