from collections import deque
import sys

input = sys.stdin.readline

q = deque()
m, n = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(m)]
visited = [[False for _ in range(n)] for _ in range(m)]


def bfs(_x, _y):
    pos = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    q.append((_x, _y))
    visited[_y][_x] = True

    while q:
        x, y = q.popleft()
        for dx, dy in pos:
            if 0 <= x+dx < n and 0 <= y+dy < m:
                if not visited[y+dy][x+dx] and g[y+dy][x+dx] == 1:
                    visited[y+dy][x+dx] = True
                    q.append((x+dx, y+dy))


ans = 0
for y in range(m):
    for x in range(n):
        if g[y][x] == 1 and not visited[y][x]:
            bfs(x, y)
            ans += 1


print(ans)
