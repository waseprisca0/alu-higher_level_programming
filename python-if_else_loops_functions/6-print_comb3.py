#!/usr/bin/python3
for l in range(0, 9 + 1):
    for n in range(0, 9 + 1):
        if l >= n:
            continue
        elif l == 8 and n == 9:
            print("{}{}".format(l, n))
        else:
            print("{}{}".format(l, n), end=', ')
