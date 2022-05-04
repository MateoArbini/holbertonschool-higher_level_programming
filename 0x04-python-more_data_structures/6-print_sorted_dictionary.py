#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary):
        element = a_dictionary.get(key)
        print(f"{key}: {element}")
