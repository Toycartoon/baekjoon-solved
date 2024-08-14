from math import gcd

n, m = map(int, input().split(":"))
g = gcd(n, m)

print(f"{n // g}:{m // g}")
