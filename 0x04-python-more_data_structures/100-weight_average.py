#!/usr/bin/python3
def weight_average(my_list=[]):
    result_sum = 0
    result_mul = 0
    result_div = 0
    average = 0
    if len(my_list) == 0:
            return 1
    for tupla in my_list:
        result_mul = tupla[0] * tupla[1]
        result_sum += result_mul
        result_div += tupla[1]
        average = result_sum / result_div
    return average
