#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    length = 0
    counter = 0
    j = 0
    ret = []
    try:
        if x <= 0:
            return counter
        else:
            for j in my_list:
                ret.append(j)
                counter += 1
                if counter < x:
                    continue
                else:
                    print(*ret, sep="", end='\n')
                    return counter
    except IndexError:
        for j in my_list:
            ret.append(j)
            counter += 1
    print(*ret, sep="", end='\n')
    return counter
