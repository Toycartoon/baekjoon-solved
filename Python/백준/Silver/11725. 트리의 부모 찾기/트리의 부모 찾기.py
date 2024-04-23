import sys

sys.setrecursionlimit(10 ** 6)

n = int(input())
t = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())

    t[a].append(b)
    t[b].append(a)


def dfs(e, r, p):
    visited[r] = p
    p = r

    for x in e:
        if visited[x] == 0:
            dfs(t[x], x, p)

dfs(t[1], 1, 0)

for v in range(2, len(visited)):
    sys.stdout.write(f"{visited[v]}\n")