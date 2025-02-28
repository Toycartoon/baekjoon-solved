from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
visited = [-1 for _ in range(n+1)]

q = deque()
def bfs(x):
    visited[x] = 0
    q.append(x)

    while q:
        x = q.popleft()

        for i in g[x]:
            if visited[i] == -1:
                visited[i] = visited[x] + 1
                q.append(i)


    return visited


for i in range(m):
    x, y = map(int, input().split())
    g[x].append(y)


visited = bfs(1)
print(visited[n])
