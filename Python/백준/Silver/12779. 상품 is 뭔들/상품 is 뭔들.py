from math import isqrt, gcd

a, b = map(int, input().split())

if isqrt(b) - isqrt(a) == 0:
    print(0)
else:
    g = gcd(isqrt(b)-isqrt(a), b-a)
    print(f"{(isqrt(b)-isqrt(a))//g}/{(b-a)//g}")
