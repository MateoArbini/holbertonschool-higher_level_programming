#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    final = []
    for i in my_list:
        if i % 2 == 0:
            value = True
            final.append(value)
        else:
            value = False
            final.append(value)
    return final
