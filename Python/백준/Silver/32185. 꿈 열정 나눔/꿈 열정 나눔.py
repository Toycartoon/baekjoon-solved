import sys

input = sys.stdin.readline

n, m = map(int, input().split())
v0, p0, s0 = map(int, input().split())
x = v0 + p0 + s0

g = []
for i in range(n):
    v, p, s = map(int, input().split())
    y = v + p + s

    if x >= y:
        g.append((y, i+1))

g.sort(key=lambda x: -x[0])
print(0, end=" ")
for i in range(min(m-1, len(g))):
    print(g[i][1], end=" ")
