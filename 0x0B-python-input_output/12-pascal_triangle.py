#!/usr/bin/python3
'''
Create a function def pascal_triangle(n): that returns
a list of lists of integers representing the Pascal’s triangle of n:

    Returns an empty list if n <= 0
    You can assume n will be always an integer
    You are not allowed to import any module
'''


def pascal_triangle(n):
    """function of pascal triangle"""
    if n == 1:
        return [[1]]
    if n <= 0:
        return []

    pascal_triang = [[1]]
    for a in range(n - 1):
        b = [1]
        for c in range(a):
            b.append(pascal_triang[-1][c] + pascal_triang[-1][c + 1])
        b.append(1)
        pascal_triang.append(b)
    return pascal_triang
