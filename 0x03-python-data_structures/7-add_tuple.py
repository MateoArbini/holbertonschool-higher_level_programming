#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = ()
    length_a = len(tuple_a)
    length_b = len(tuple_b)
    if(type(tuple_c) == type(tuple_a) and type(tuple_c) == type(tuple_b)):
        if(length_a < 2 and length_a != 0):
            for i in range(0, length_a):
                tuple_a = tuple_a + (0, )
        elif(length_b < 2 and length_b != 0):
            for j in range(0, length_b):
                tuple_b = tuple_b + (0, )
        elif(length_a == 0):
            tuple_a = tuple_a + (0, 0)
        elif(length_b == 0):
            tuple_b = tuple_b + (0, 0)

    for h in tuple_a:
        for k in tuple_b:
            tuple_c = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    return tuple_c
