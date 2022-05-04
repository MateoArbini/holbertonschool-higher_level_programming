#!/usr/bin/python3
def search_replace(my_list, search, replace):
    final = []
    for i in my_list:
        if i == search:
            i = replace
            final.append(i)
        else:
            final.append(i)
    return final
