#!/usr/bin/python3
import json
'''
Write a function that creates an Object from a “JSON file”:

    Prototype: def load_from_json_file(filename):
    You must use the with statement
    You don’t need to manage exceptions if the JSON string doesn’t
    represent an object.
    You don’t need to manage file permissions / exceptions.
'''


def load_from_json_file(filename):
    '''function'''
    with open(filename, encoding="utf-8") as f:
        my_data = json.load(f)
    return my_data
