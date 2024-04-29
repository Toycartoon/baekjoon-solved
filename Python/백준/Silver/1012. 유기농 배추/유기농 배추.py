from collections import deque


def bfs(x, y):
    q = deque()
    pos = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    q.append((x, y))

    while q:
        x, y = q.popleft()
        visited[y][x] = True

        for dx, dy in pos:
            if 0 <= x + dx < m and 0 <= y + dy < n:
                if not visited[y+dy][x+dx] and g[y+dy][x+dx] == 1:
                    visited[y+dy][x+dx] = True
                    q.append((x+dx, y+dy))


for t in range(int(input())):
    m, n, k = map(int, input().split())
    g = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    for i in range(k):
        x, y = map(int, input().split())
        g[y][x] = 1

    ans = 0
    for y in range(n):
        for x in range(m):
            if not visited[y][x] and g[y][x] == 1:
                bfs(x, y)
                ans += 1

    print(ans)
