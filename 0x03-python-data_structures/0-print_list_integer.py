#!/usr/bin/python3
def print_list_integer(my_list=[]):
    a = []
    if type(a) == type(my_list):
        for i in my_list:
            print(f"{i}", end='\n')
    return my_list
