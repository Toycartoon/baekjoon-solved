from collections import deque


n, m, a, b = map(int, input().split())
visited = [False for i in range(n+1)]

for i in range(m):
    l, r = map(int, input().split())
    for x in range(l, r+1):
        visited[x] = True

q = deque()
def bfs(s):
    q.append((s, 0))
    visited[s] = True

    while q:
        x, c = q.popleft()

        if x == n:
            return c

        if x + a <= n and not visited[x + a]:
            visited[x + a] = True
            q.append((x+a, c+1))
        if x + b <= n and not visited[x + b]:
            visited[x + b] = True
            q.append((x+b, c+1))

    return -1


print(bfs(0))
