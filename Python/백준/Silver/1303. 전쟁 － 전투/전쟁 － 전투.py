from collections import deque


def bfs(_x, _y, type):
    pos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    c = 1

    visited[_y][_x] = True
    q.append((_x, _y))

    while q:
        x, y = q.popleft()

        for dx, dy in pos:
            if 0 <= x + dx < n and 0 <= y + dy < m:
                if g[y+dy][x+dx] == type and not visited[y+dy][x+dx]:
                    c += 1
                    visited[y+dy][x+dx] = True
                    q.append((x+dx, y+dy))

    return c


n, m = map(int, input().split())
g = [input() for _ in range(m)]
visited = [[False] * n for _ in range(m)]

b, w = 0, 0
q = deque()

for y in range(m):
    for x in range(n):
        if not visited[y][x]:
            if g[y][x] == "B":
                b += bfs(x, y, "B") ** 2
            elif g[y][x] == "W":
                w += bfs(x, y, "W") ** 2


print(w, b)
