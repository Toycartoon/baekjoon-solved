from math import isqrt

n = int(input())
if isqrt(n) ** 2 != n:
    print(isqrt(n)+1)
else:
    print(isqrt(n))
