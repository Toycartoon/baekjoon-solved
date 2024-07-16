import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
g = [[] for _ in range(n)]
visited = [False] * n

for _ in range(m):
    u, v = map(int, input().split())

    g[u - 1].append(v-1)
    g[v - 1].append(u-1)


q = deque()
def bfs(s):
    visited[s] = True
    q.append(s)

    while q:
        x = q.popleft()

        for v in g[x]:
            if not visited[v]:
                visited[v] = True
                q.append(v)


ans = 0
for i in range(n):
    if not visited[i]:
        bfs(i)
        ans += 1


print(ans)
