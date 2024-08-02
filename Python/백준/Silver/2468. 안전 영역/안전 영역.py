from collections import deque

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]


q = deque()
def bfs(_x, _y):
    visited[_y][_x] = True
    pos = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    q.append((_x, _y))
    while q:
        x, y = q.popleft()

        for dx, dy in pos:
            if 0 <= x + dx < n and 0 <= y + dy < n:
                if not visited[y + dy][x + dx] and g[y + dy][x + dx] > v:
                    visited[y + dy][x + dx] = True
                    q.append((x + dx, y + dy))


ans = 1
v = 1
while True:
    c = 0
    visited = [[False] * n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if g[y][x] > v and not visited[y][x]:
                bfs(x, y)
                c += 1

    if c == 0:
        break

    ans = max(c, ans)
    v += 1


print(ans)
