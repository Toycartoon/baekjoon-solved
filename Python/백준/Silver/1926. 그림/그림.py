from collections import deque


def bfs(_x, _y):
    q = deque()
    visited[_y][_x] = True
    pos = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    c = 1

    q.append((_x, _y))
    while q:
        x, y = q.popleft()
        for dx, dy in pos:
            if 0 <= x + dx < m and 0 <= y + dy < n:
                if not visited[y+dy][x+dx] and g[y+dy][x+dx] == 1:
                    visited[y+dy][x+dx] = True
                    q.append((x+dx, y+dy))
                    c += 1

    return c


n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

ans = []
for y in range(n):
    for x in range(m):
        if g[y][x] == 1 and not visited[y][x]:
            r = bfs(x, y)

            ans.append(r)

print(len(ans))
if len(ans) == 0:
    ans.append(0)
print(max(ans))
