from collections import deque

f, s, g, u, d = map(int, input().split())
q = deque()
visited = [False for _ in range(f+1)]

def bfs(x):
    visited[x] = True
    q.append((0, x))

    while q:
        c, x = q.popleft()

        if x == g:
            return c

        if x + u <= f:
            if not visited[x+u]:
                visited[x+u] = True
                q.append((c+1, x+u))
        if x - d >= 1:
            if not visited[x-d]:
                visited[x-d] = True
                q.append((c+1, x-d))

    return -1


ans = bfs(s)
if ans == -1:
    print("use the stairs")
else:
    print(ans)
