from collections import deque


def normal_bfs(_x, _y, c):
    q = deque()
    n_visited[_y][_x] = True
    pos = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    q.append((_x, _y))

    while q:
        x, y = q.popleft()
        for dx, dy in pos:
            if 0 <= x + dx < n and 0 <= y + dy < n:
                if g[y + dy][x + dx] == c and not n_visited[y + dy][x + dx]:
                    n_visited[y + dy][x + dx] = True
                    q.append((x + dx, y + dy))


def cw_bfs(_x, _y, c):
    q = deque()
    cw_visited[_y][_x] = True
    pos = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    q.append((_x, _y))

    while q:
        x, y = q.popleft()
        for dx, dy in pos:
            if 0 <= x + dx < n and 0 <= y + dy < n:
                if (g[y + dy][x + dx] == c or ((g[y + dy][x + dx] == "R" and c == "G") or (g[y + dy][x + dx] == "G" and c == "R"))) and not cw_visited[y + dy][x + dx]:
                    cw_visited[y + dy][x + dx] = True
                    q.append((x + dx, y + dy))

n = int(input())
g = [[*input()] for _ in range(n)]
n_visited = [[False] * n for _ in range(n)]
cw_visited = [[False] * n for _ in range(n)]

n_ans = 0
cw_ans = 0
for y in range(n):
    for x in range(n):
        if not n_visited[y][x]:
            normal_bfs(x, y, g[y][x])
            n_ans += 1
        if not cw_visited[y][x]:
            cw_bfs(x, y, g[y][x])
            cw_ans += 1


print(n_ans, cw_ans)
