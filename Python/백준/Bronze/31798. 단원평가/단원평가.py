from math import isqrt

a, b, c = map(int, input().split())

if c == 0:
    print(isqrt(a + b))
else:
    print(c ** 2 - a - b)