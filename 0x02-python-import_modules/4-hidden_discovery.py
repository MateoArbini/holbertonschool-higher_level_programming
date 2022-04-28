#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    array = dir(hidden_4)
    for i in array:
        if(i[0] == "_" and i[1] == "_"):
            continue
        else:
            print(i)
