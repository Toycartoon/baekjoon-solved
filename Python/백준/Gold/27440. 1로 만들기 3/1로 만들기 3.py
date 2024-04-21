from collections import deque

visited = {}
q = deque()


def bfs(r):
    visited[r] = True

    q.append((r, 0))
    while q:
        x, c = q.popleft()
        if x == 1:
            return c
        if x % 3 == 0 and x // 3 not in visited:
            visited[x // 3] = True
            q.append((x // 3, c+1))
        if x % 2 == 0 and x // 2 not in visited:
            visited[x // 2] = True
            q.append((x // 2, c+1))
        if x - 1 not in visited:
            visited[x-1] = True
            q.append((x-1, c+1))


n = int(input())
print(bfs(n))