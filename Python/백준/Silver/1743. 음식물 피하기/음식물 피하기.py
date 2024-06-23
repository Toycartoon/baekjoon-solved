from collections import deque

n, m, k = map(int, input().split())
g = [["."] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

for i in range(k):
    r, c = map(int, input().split())
    g[r-1][c-1] = "#"

q = deque()
def bfs(_x, _y):
    c = 1
    visited[_y][_x] = True
    q.append((_x, _y))

    pos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while q:
        x, y = q.popleft()

        for dy, dx in pos:
            if 0 <= x+dx < m and 0 <= y+dy < n:
                if not visited[y+dy][x+dx] and g[y+dy][x+dx] == "#":
                    visited[y+dy][x+dx] = True
                    q.append((x+dx, y+dy))
                    c += 1

    return c


ans = []
for y in range(n):
    for x in range(m):
        if g[y][x] == "#" and not visited[y][x]:
            ans.append(bfs(x, y))

print(max(ans))
