#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    a = [[]]
    if(type(a) == type(matrix)):
        for i in matrix:
            for j in i:
                print(f"{j:d}", end=' ')
            print('', end='\n')
