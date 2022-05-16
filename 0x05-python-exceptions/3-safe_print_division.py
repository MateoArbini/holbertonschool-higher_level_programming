#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    if type(a) is int and type(b) is int:
        try:
            result = a / b
            return result
        except ZeroDivisionError:
            result = None
            return result

        finally:
            print("Inside result: {}".format(result))
