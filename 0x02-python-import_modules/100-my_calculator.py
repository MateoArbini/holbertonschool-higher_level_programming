#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    sum = 0
    argc = len(sys.argv)
    argv = sys.argv
    if(argc - 1 != 3):
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        if(argv[2] == "+"):
            print(f"{a} {argv[2]} {b} = {add(a, b)}")
        elif(argv[2] == "-"):
            print(f"{a} {argv[2]} {b} = {sub(a, b)}")
        elif(argv[2] == "*"):
            print(f"{a} {argv[2]} {b} = {mul(a, b)}")
        elif(argv[2] == "/"):
            print(f"{a} {argv[2]} {b} = {div(a, b)}")
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
