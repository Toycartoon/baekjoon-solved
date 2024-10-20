from collections import deque
from math import inf


r, c = map(int, input().split())
g = [[*input()] for _ in range(r)]

q = deque()


def bfs(_x, _y, visited):
    pos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited[_y][_x] = 0
    q.append((_x, _y))

    while q:
        x, y = q.popleft()

        for dx, dy in pos:
            if 0 <= x + dx < c and 0 <= y + dy < r:
                if g[y+dy][x+dx] == "0" and visited[y+dy][x+dx] == inf:
                    visited[y+dy][x+dx] = visited[y][x] + 1
                    q.append((x+dx, y+dy))

    return visited


ny, nx = map(int, input().split())
sy, sx = map(int, input().split())
cy, cx = map(int, input().split())

nucksal = bfs(nx-1, ny-1, [[inf] * c for _ in range(r)])
swings = bfs(sx-1, sy-1, [[inf] * c for _ in range(r)])
changmo = bfs(cx-1, cy-1, [[inf] * c for _ in range(r)])

ans_g = [[0] * c for _ in range(r)]
for y in range(r):
    for x in range(c):
        ans_g[y][x] = max(nucksal[y][x], swings[y][x], changmo[y][x])


min_t = inf
ans = 0
for y in range(r):
    for x in range(c):
        if ans_g[y][x] < min_t:
            min_t = ans_g[y][x]
            ans = 1
        elif ans_g[y][x] == min_t:
            ans += 1


if min_t == inf:
    print(-1)
else:
    print(min_t)
    print(ans)
