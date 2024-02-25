from collections import deque

visited = [False] * 100001
n, k = map(int, input().split())

q = deque()

def bfs(r):
    visited[r] = True
    q.append((r, 0))
    while q:
        x, c = q.popleft()
        if x == k:
            return c
        if x + 1 <= 100000:
            if not visited[x+1]:
                visited[x+1] = True
                q.append((x+1, c+1))
        if x - 1 >= 0 and not visited[x-1]:
            visited[x-1] = True
            q.append((x-1, c+1))
        if 2 * x <= 100000:
            if not visited[2*x]:
                visited[x * 2] = True
                q.append((x*2, c+1))


print(bfs(n))
