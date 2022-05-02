#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        length = len(i)
        count = 0
        for j in i:
            print(f"{j:d}", end='')
            if count < length - 1:
                print(' ', end='')
            count += 1
        print("")
