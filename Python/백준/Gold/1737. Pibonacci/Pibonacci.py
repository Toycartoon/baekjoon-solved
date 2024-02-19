import sys
from math import pi

sys.setrecursionlimit(10 ** 6)

n = int(input())

m = {0: 1}

def p(n):
    global m

    if n <= pi:
        return m[0]
    if n in m:
        return m[n]
    v = p(n - 1) + p(n - pi)
    m[n] = v
    return m[n]

print(p(n) % 1000000000000000000)