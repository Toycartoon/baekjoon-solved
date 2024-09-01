from collections import deque


n, m = map(int, input().split())
g = [i for i in range(101)]
visited = [False for _ in range(101)]

q = deque()
def bfs(x, c):
    visited[x] = True
    q.append((x, c))

    while q:
        i, cost = q.popleft()

        if i == 100:
            return cost
        
        for j in range(1, 7):
            if i + j <= 100 and not visited[i + j]:
                visited[i + j] = True
                q.append((g[i + j], cost + 1))


for _ in range(n):
    x, y = map(int, input().split())
    g[x] = y

for _ in range(m):
    u, v = map(int, input().split())
    g[u] = v


print(bfs(1, 0))
