import sys
from math import inf, isinf

input = sys.stdin.readline

n = int(input())
mn = inf
for i in range(n):
    m, o = map(int, input().split())

    if o == 0:
        mn = min(mn, m)

print(mn if not isinf(mn) else -1)
