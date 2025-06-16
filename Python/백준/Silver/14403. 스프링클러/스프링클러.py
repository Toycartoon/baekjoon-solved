import sys
from math import inf

input = sys.stdin.readline

n, x1, y1, x2, y2 = map(int, input().split())

g = []
for i in range(n):
    x, y = map(int, input().split())

    d1 = (x-x1) ** 2 + (y-y1) ** 2
    d2 = (x-x2) ** 2 + (y-y2) ** 2

    g.append((d1, d2))

ans = max(g, key=lambda x: x[0])[0]
g.sort()
for i in range(n-1):
    ans = min(g[i][0] + max(g[i+1:], key=lambda x: x[1])[1], ans)

g.sort(key=lambda x: x[1])
for i in range(n-1):
    ans = min(g[i][1] + max(g[i+1:], key=lambda x: x[0])[0], ans)

ans = min(max(g, key=lambda x: x[1])[1], ans)
print(int(ans))
