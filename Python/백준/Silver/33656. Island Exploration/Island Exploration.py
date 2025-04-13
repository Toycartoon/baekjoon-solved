from collections import deque

r, c = map(int, input().split())
g = [[*input()] for _ in range(r)]
visited = [[False for _ in range(c)] for __ in range(r)]

q = deque()

def bfs(_x, _y):
    pos = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    q.append((_x, _y))
    visited[_y][_x] = True

    ans = 1
    while q:
        x, y = q.popleft()

        for dx, dy in pos:
            if 0 <= x+dx < c and 0 <= y+dy < r:
                if g[y+dy][x+dx] == "#" and not visited[y+dy][x+dx]:
                    visited[y+dy][x+dx] = True
                    q.append((x+dx, y+dy))
                    ans += 1

    return ans


for y in range(r):
    for x in range(c):
        if g[y][x] == "S":
            print(bfs(x, y))
            break
