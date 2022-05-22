#!/usr/bin/python3
'''
function that divides all elements of a matrix
'''


def matrix_divided(matrix, div):
    '''function'''
    length1 = len(matrix[0])
    length2 = len(matrix[1])
    message = "matrix must be a matrix (list of lists) of integers/floats"

    if type(div) is not float and type(div) is not int:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if length1 != length2:
        raise TypeError("Each row of the matrix must have the same size")
    if type(matrix) is not list:
        raise TypeError(message)
    if matrix is None or len(matrix[0]) == 0 or len(matrix) == 0:
        raise TypeError(message)

    new_matrix = []
    for lists in matrix:
        if type(lists) is not list:
            raise TypeError(message)
        if len(lists) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        first_element = []
        for element in lists:
            if type(element) is not int and type(element) is not float:
                raise TypeError(message)
            else:
                element = element / div
                first_element.append(round(element, 2))
        new_matrix.append(first_element)
    return new_matrix
