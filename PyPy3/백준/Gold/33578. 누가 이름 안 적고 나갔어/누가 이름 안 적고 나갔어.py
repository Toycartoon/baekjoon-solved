from collections import deque
from math import inf
import sys

input = sys.stdin.readline

q = deque()
def bfs(_x, _y):
    pos = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    visited[_y][_x] = 0
    q.append((_x, _y, 2))

    while q:
        x, y, c = q.popleft()

        for dx, dy in pos:
            if 0 <= x+dx < m and 0 <= y+dy < n:
                if g[y+dy][x+dx] != "#" and visited[y+dy][x+dx] > c:
                    visited[y+dy][x+dx] = c
                    q.append((x+dx, y+dy, c+2))


tq = deque()
def teacher(_x, _y):
    pos = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    t[_y][_x] = 0
    tq.append((_x, _y, 1))

    while tq:
        x, y, c = tq.popleft()

        for dx, dy in pos:
            if 0 <= x+dx < m and 0 <= y+dy < n:
                if g[y+dy][x+dx] != "#" and t[y+dy][x+dx] > c:
                    t[y+dy][x+dx] = c
                    tq.append((x+dx, y+dy, c+1))


n, m = map(int, input().split())
g = [[*input().strip()] for _ in range(n)]
visited = [[inf for _ in range(m)] for _ in range(n)]
t = [[inf for _ in range(m)] for _ in range(n)]

sx, sy = -1, -1
jx, jy = -1, -1
for y in range(n):
    for x in range(m):
        if g[y][x] == "S":
            sx, sy = x, y
        elif g[y][x] == "J":
            jx, jy = x, y


bfs(jx, jy)
teacher(sx, sy)
ans = [visited[sy][sx]]

for y in range(n):
    for x in range(m):
        if g[y][x] == "T":
            ans.append(visited[y][x] + t[y][x])

print(min(ans) if min(ans) != inf else -1)
