import sys

sys.setrecursionlimit(10 ** 6)

n, m, r = map(int, input().split())
g = [[] for _ in range(n)]
visited = [-1 for _ in range(n)]


def dfs(e, r, d):
    visited[r] = d
    d += 1

    for x in e:
        if visited[x] == -1:
            dfs(g[x], x, d)


for i in range(m):
    u, v = map(int, sys.stdin.readline().split())

    g[u - 1].append(v - 1)
    g[v - 1].append(u - 1)

for j in range(n):
    g[j] = sorted(g[j], reverse=True)

dfs(g[r - 1], r - 1, 0)

for l in visited:
    sys.stdout.write(f"{l}\n")