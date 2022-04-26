#!/usr/bin/python3
for i in range(0, 10):
    for e in range(i, 10):
        if (i == e):
            continue
        elif (i == 8 and e == 9):
            print("{}{}".format(i, e), end='\n')
        elif (i != e):
            print("{}{}".format(i, e), end=', ')
