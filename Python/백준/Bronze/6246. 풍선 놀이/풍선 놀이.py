n, q = map(int, input().split())
g = [False for _ in range(n)]

for _ in range(q):
    l, i = map(int, input().split())
    for x in range(l-1, n, i):
        g[x] = True

print(g.count(False))
