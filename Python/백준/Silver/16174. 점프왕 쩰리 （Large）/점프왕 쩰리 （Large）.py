from collections import deque

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

q = deque()
def bfs(_x, _y):
    pos = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    visited[_y][_x] = True
    q.append((_x, _y))

    while q:
        x, y = q.popleft()

        for dx, dy in pos:
            if 0 <= x + g[y][x] * dx < n and 0 <= y + g[y][x] * dy < n:
                if not visited[y+g[y][x]*dy][x+g[y][x]*dx]:
                    visited[y+g[y][x]*dy][x+g[y][x]*dx] = True
                    q.append((x + g[y][x] * dx, y + g[y][x] * dy))


bfs(0, 0)
if visited[-1][-1]:
    print("HaruHaru")
else:
    print("Hing")
