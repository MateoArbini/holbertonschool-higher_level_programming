#!/usr/bin/python3
for i in range(0, 26):
    letter = ord('z') - i
    if (i % 2 == 1):
        letter = chr(letter - ord('a') + ord('A'))
    else:
        letter = chr(letter)
    print(letter, end='')
