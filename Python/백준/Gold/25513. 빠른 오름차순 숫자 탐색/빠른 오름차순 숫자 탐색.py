from collections import deque


g = [list(map(int, input().split())) for _ in range(5)]
visited = [[0] * 5 for _ in range(5)]
r, c = map(int, input().split())


def bfs(_x, _y, n):
    q = deque()
    visited = [[0] * 5 for _ in range(5)]

    visited[_y][_x] = 0
    q.append((_x, _y))

    pos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while q:
        x, y = q.popleft()

        if 0 <= x < 5 and 0 <= y < 5:
            if g[y][x] == n:
                return visited, x, y

        for dx, dy in pos:
            if 0 <= x+dx < 5 and 0 <= y+dy < 5:
                if visited[y+dy][x+dx] == 0 and g[y+dy][x+dx] != -1:
                    visited[y+dy][x+dx] = visited[y][x] + 1
                    q.append((x+dx, y+dy))


ans = 0
for i in range(1, 7):
    try:
        visited, x, y = bfs(c, r, i)

        ans += visited[y][x]
        r, c = y, x
        visited = [[0] * 5 for _ in range(5)]
    except TypeError:
        print(-1)
        exit()

print(ans)
