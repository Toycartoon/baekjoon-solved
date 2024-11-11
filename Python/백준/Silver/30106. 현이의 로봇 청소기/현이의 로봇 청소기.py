from collections import deque


def bfs(_x, _y):
    pos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    q.append((_x, _y))
    visited[_y][_x] = True

    while q:
        x, y = q.popleft()

        for dx, dy in pos:
            if 0 <= x + dx < m and 0 <= y + dy < n:
                if abs(g[y][x] - g[y+dy][x+dx]) <= k and not visited[y+dy][x+dx]:
                    visited[y+dy][x+dx] = True
                    q.append((x+dx, y+dy))


q = deque()
n, m, k = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

ans = 0
for y in range(n):
    for x in range(m):
        if not visited[y][x]:
            bfs(x, y)
            ans += 1

print(ans)
