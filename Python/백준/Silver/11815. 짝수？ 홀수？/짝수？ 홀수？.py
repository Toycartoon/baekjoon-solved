from math import isqrt

n = int(input())
a = list(map(int, input().split()))

for x in a:
    print(int(isqrt(x) ** 2 == x), end=" ")
