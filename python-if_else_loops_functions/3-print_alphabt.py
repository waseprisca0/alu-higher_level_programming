#!/usr/bin/python3
for let in range(ord('a'), ord('z') + 1):
    if chr(let) != 'q' and chr(let) != 'e':
        print("{}".format(chr(let)), end='')
