import sys, collections

sys.setrecursionlimit(10 ** 6)

n, m, r = map(int, input().split())
g = [[] for _ in range(n)]
visited = [0 for _ in range(n)]
q = collections.deque()
c = 0


def bfs(r):
    global c

    visited[r] = c + 1
    c += 1

    q.append(r)
    while len(q) != 0:
        y = q.popleft()
        for x in g[y]:
            if visited[x] == 0:
                visited[x] = c + 1
                c += 1
                q.append(x)


for i in range(m):
    u, v = map(int, sys.stdin.readline().split())

    g[u - 1].append(v - 1)
    g[v - 1].append(u - 1)

for j in range(n):
    g[j] = sorted(g[j], reverse=True)

bfs(r - 1)

for l in visited:
    print(l)