#!/usr/bin/python3
import json
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
'''
Write a script that adds all arguments to a Python list, and then save
them to a file:

    You must use your function save_to_json_file from 5-save_to_json_file.py
    You must use your function load_from_json_file from
    6-load_from_json_file.py
    The list must be saved as a JSON representation in a file named
    add_item.json
    If the file doesn’t exist, it should be created
    You don’t need to manage file permissions / exceptions.
'''


fname = "add_item.json"

try:
    load = load_from_json_file(fname)
except FileNotFoundError:
    load = []

save_to_json_file(load + argv[1:], fname)
