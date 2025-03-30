import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
g = [[*input().strip()] for _ in range(n)]
visited = [[False for _ in range(m)] for __ in range(n)]

q = deque()
def bfs(_x, _y):
    pos = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    visited[_y][_x] = True
    c = 1
    q.append((_x, _y))

    while q:
        x, y = q.popleft()

        for dx, dy in pos:
            if 0 <= x+dx < m and 0 <= y+dy < n:
                if not visited[y+dy][x+dx] and g[y+dy][x+dx] == ".":
                    visited[y+dy][x+dx] = True
                    c += 1
                    q.append((x+dx, y+dy))


    return c


ans = []
for y in range(n):
    for x in range(m):
        if g[y][x] == "." and not visited[y][x]:
            ans.append(bfs(x, y))


if len(ans) == 0:
    print(-1)
else:
    print(max(ans))
