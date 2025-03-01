from collections import deque


n = int(input())
a, b = map(int, input().split())
m = int(input())

g = [[] for _ in range(n+1)]
visited = [-1 for _ in range(n+1)]

q = deque()
def bfs(x):
    q.append(x)
    visited[x] = 0

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
    g[y].append(x)


visited = bfs(a)
print(visited[b])
