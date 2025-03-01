import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
g = [[] for _ in range(n+1)]

q = deque()
def bfs(x):
    visited = [-1 for _ in range(n+1)]
    q.append(x)
    visited[x] = 0

    while q:
        x = q.popleft()

        for i in g[x]:
            if visited[i] == -1:
                visited[i] = visited[x] + 1
                q.append(i)

    return sum(visited[1:])


for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

ans = []
for i in range(1, n+1):
    ans.append(bfs(i))

print(ans.index(min(ans))+1)
