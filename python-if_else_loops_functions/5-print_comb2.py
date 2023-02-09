#!/usr/bin/python3
for t in range(00, 99 + 1):
    if t == 99:
        print("{}".format(t))
    else:
        print("{:02}".format(t), end=', ')
