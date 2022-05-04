#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    def potencia(lista):
        result = list(map(lambda x: x ** 2 , lista))
        return result
    final = list(map(potencia, matrix))
    return final

