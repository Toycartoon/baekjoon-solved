m, n = map(int, input().split())
g = [False for _ in range(m)]

for i in range(n):
    l, r = map(int, input().split())
    for x in range(l-1, r):
        g[x] = True

if g.count(True) == m:
    print("YES")
else:
    print("NO")
