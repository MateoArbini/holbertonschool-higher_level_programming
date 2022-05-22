#!/usr/bin/python3
'''
function that prints a text with 2 new lines after each of these
characters: ., ? and :
'''

def text_indentation(text):
    '''function'''
    if type(text) is not str:
        raise TypeError("text must be a string")

    new_string = text.replace('. ', '.\n\n')
    new_string1 = new_string.replace('? ', '?\n\n')
    new_string2 = new_string1.replace(': ', ':\n\n')
    print(new_string2, end='') 
