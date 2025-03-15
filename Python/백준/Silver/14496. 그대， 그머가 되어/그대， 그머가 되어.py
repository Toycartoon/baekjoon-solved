from collections import deque
import sys

input = sys.stdin.readline

q = deque()
a, b = map(int, input().split())
n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
visited = [-1 for _ in range(n + 1)]

for i in range(m):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)

def bfs(x):
    visited[x] = 0
    q.append(x)

    while q:
        x = q.popleft()

        for i in g[x]:
            if visited[i] == -1:
                visited[i] = visited[x] + 1
                q.append(i)

bfs(a)
print(visited[b])
