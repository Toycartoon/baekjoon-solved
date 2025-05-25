from collections import deque
import sys

input = sys.stdin.readline

q = deque()
def bfs(_x):
    visited[_x] = True

    q.append(_x)
    while q:
        x = q.popleft()

        for i in g[x]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

    return visited.count(True) - k - 1

n, m, k = map(int, input().split())
g = [[] for _ in range(n+2)]
visited = [False for _ in range(n+2)]

for i in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

for i in map(int, input().split()):
    visited[i] = True

print(bfs(1))
