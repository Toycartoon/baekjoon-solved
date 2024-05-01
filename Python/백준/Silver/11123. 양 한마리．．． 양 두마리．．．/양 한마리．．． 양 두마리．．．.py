from collections import deque


def bfs(x, y):
    q = deque()
    pos = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    visited[y][x] = True
    q.append((x, y))
    while q:
        _x, _y = q.popleft()
        for dx, dy in pos:
            if 0 <= _x + dx < w and 0 <= _y + dy < h:
                if not visited[_y + dy][_x + dx] and g[_y + dy][_x + dx] == "#":
                    visited[_y + dy][_x + dx] = True
                    q.append((_x+dx, _y+dy))


for t in range(int(input())):
    h, w = map(int, input().split())
    g = [[*input()] for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    ans = 0
    for y in range(h):
        for x in range(w):
            if g[y][x] == "#" and not visited[y][x]:
                bfs(x, y)
                ans += 1

    print(ans)
