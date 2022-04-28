#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if((len(sys.argv) - 1) == 0):
        print(f"{len(sys.argv) - 1} arguments.")
    elif((len(sys.argv) - 1 == 1)):
        print(f"{len(sys.argv) - 1} argument:")
    else:
        print(f"{len(sys.argv) - 1} arguments:")
    for argument in range(1, len(sys.argv)):
        print(f"{argument}: {sys.argv[argument]}")
