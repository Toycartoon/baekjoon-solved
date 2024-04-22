import sys, collections

sys.setrecursionlimit(10 ** 6)

n, m, r = map(int, input().split())
g = [[] for _ in range(n)]
visited = [-1 for _ in range(n)]
q = collections.deque()


def bfs(r, d):
    visited[r] = d
    d += 1

    q.append(r)
    while len(q) != 0:
        y = q.popleft()
        depth = visited[y]
        for x in g[y]:
            if visited[x] == -1:
                visited[x] = depth + 1
                q.append(x)


for i in range(m):
    u, v = map(int, sys.stdin.readline().split())

    g[u - 1].append(v - 1)
    g[v - 1].append(u - 1)

for j in range(n):
    g[j] = sorted(g[j])

bfs(r - 1, 0)

for l in visited:
    print(l)