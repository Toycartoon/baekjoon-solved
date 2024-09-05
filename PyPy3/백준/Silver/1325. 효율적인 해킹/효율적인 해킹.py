import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
ans = [0] * n

q = deque()
def bfs(x):
    visited[x] = True
    q.append(x)
    c = 1

    while q:
        x = q.popleft()

        for i in g[x]:
            if not visited[i]:
                visited[i] = True
                c += 1
                q.append(i)

    return c


for _ in range(m):
    a, b = map(int, input().split())

    g[b].append(a)


for i in range(n):
    visited = [False for _ in range(n + 1)]
    ans[i] = bfs(i+1)

a = max(ans)
for i in range(n):
    if a == ans[i]:
        print(i+1, end=" ")
