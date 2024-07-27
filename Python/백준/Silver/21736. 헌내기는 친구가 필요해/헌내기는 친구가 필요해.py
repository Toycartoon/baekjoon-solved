from collections import deque

n, m = map(int, input().split())
g = [[*input()] for _ in range(n)]
visited = [[False] * m for _ in range(n)]

q = deque()
def bfs(_x, _y):
    pos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    q.append((_x, _y))
    ans = 0

    while q:
        x, y = q.popleft()
        for dx, dy in pos:
            if 0 <= x + dx < m and 0 <= y + dy < n:
                if g[y + dy][x + dx] != "X" and not visited[y + dy][x + dx]:
                    if g[y + dy][x + dx] == "P":
                        ans += 1
                    visited[y + dy][x + dx] = True
                    q.append((x + dx, y + dy))

    return ans if ans != 0 else "TT"


ix, iy = 0, 0
for y in range(n):
    for x in range(m):
        if g[y][x] == "I":
            ix, iy = x, y
            break

print(bfs(ix, iy))
