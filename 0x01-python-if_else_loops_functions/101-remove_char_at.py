#!/usr/bin/python3
def remove_char_at(str, n):
    str_tot = str
    if (str):
        str = str[:n] + str[n + 1:]
    if(n < 0):
        str = str_tot
    return(str)
