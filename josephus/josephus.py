#!/usr/bin/env python3.9

def josephus(n):
    x = 0
    while (2 ** x) < n:
        x += 1
    l = n - (2 ** (x-1))
    w = (2 * l) + 1
    print(f'Winning seat is {w}')
    return x
