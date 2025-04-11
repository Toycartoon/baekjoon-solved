import sys

input = sys.stdin.readline

n, q = map(int, input().split())
g = [0 for _ in range(n+1)]

for i in range(q):
    c, p, x = map(int, input().split())

    if c == 1:
        for a in range(p, n+1):
            g[a] += x
    elif c == 2:
        print(g[x] - g[p-1])
