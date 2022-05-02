#!/usr/bin/env python3
def no_c(my_string):
    new = my_string.translate({ord('c'): None})
    aux = new
    aux = new.translate({ord('C'): None})
    return aux
