import sys

sys.setrecursionlimit(10 ** 6)

n, m, r = map(int, input().split())
g = [[] for _ in range(n)]
visited = [0 for _ in range(n)]
c = 0


def dfs(e, r):
    global c

    visited[r] = c + 1
    c += 1

    for x in e:
        if visited[x] == 0:
            dfs(g[x], x)


for i in range(m):
    u, v = map(int, sys.stdin.readline().split())

    g[u - 1].append(v - 1)
    g[v - 1].append(u - 1)

for j in range(n):
    g[j] = sorted(g[j], reverse=True)

dfs(g[r - 1], r - 1)

for l in visited:
    sys.stdout.write(f"{l}\n")