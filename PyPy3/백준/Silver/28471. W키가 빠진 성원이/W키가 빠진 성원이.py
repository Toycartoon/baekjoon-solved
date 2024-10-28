from collections import deque


n = int(input())
g = [input() for _ in range(n)]
visited = [[False] * n for _ in range(n)]

q = deque()
sx, sy = -1, -1
for y in range(n):
    for x in range(n):
        if g[y][x] == "F":
            sx, sy = x, y
            break


def bfs(_x, _y):
    pos = [(0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    visited[_y][_x] = True
    q.append((_x, _y))
    c = 0
    while q:
        x, y = q.popleft()
        
        for dx, dy in pos:
            if 0 <= x+dx < n and 0 <= y+dy < n:
                if g[y+dy][x+dx] == "." and not visited[y+dy][x+dx]:
                    visited[y+dy][x+dx] = True
                    q.append((x+dx, y+dy))
                    c += 1

    return c


print(bfs(sx, sy))