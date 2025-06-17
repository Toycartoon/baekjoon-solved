import sys
from math import isqrt

input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    print(int(isqrt(n) ** 2 == n))
