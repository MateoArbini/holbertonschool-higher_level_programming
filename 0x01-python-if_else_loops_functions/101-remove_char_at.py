#!/usr/bin/python3
def remove_char_at(str, n):
    if (str):
        str = str[:n] + str[n + 1:]
    if(n < 0):
        str = str
    return(str)
