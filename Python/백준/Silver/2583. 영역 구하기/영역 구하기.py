from collections import deque

m, n, k = map(int, input().split())
g = [[True] * n for _ in range(m)]

for i in range(k):
    a, b, c, d = map(int, input().split())
    for y in range(b, d):
        for x in range(a, c):
            g[y][x] = False

q = deque()


def bfs(_x, _y):
    q.append((_x, _y))
    pos = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    g[_y][_x] = False
    c = 1
    while q:
        x, y = q.popleft()
        for dx, dy in pos:
            if 0 <= x+dx < n and 0 <= y+dy < m:
                if g[y+dy][x+dx]:
                    g[y+dy][x+dx] = False
                    c += 1
                    q.append((x+dx, y+dy))

    return c


ans = []
for y in range(m):
    for x in range(n):
        if g[y][x]:
            c = bfs(x, y)
            ans.append(c)


ans.sort()
print(len(ans))
print(*ans)
