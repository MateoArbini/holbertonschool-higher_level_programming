#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    final = []
    for i in range(0, list_length):
        try:
            final.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            print("wrong type")
            final.append(0)
            continue
        except ZeroDivisionError:
            print("division by zero")
            final.append(0)
            continue
        except IndexError:
            print("out of range")
            final.append(0)
            continue
    return final
