import sys
from math import sqrt

input = sys.stdin.readline
g = []

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    g.append((x, y))

print(sqrt((g[0][0] - g[-1][0]) ** 2 + (g[0][1] - g[-1][1]) ** 2))
