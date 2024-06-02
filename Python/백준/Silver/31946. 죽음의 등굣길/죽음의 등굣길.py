from collections import deque


n = int(input())
m = int(input())
g = [list(map(int, input().split())) for i in range(n)]
x = int(input())

q = deque()


def bfs(_y, _x, visited):
    visited[_y][_x] = True
    q.append((_y, _x))
    while q:
        dy, dx = q.popleft()
        for nx in range(-x, x+1):
            for ny in range(-x, x+1):
                if 0 <= dx+nx < m and 0 <= dy+ny < n and abs(nx) + abs(ny) <= x:
                    if g[dy+ny][dx+nx] == f and not visited[dy+ny][dx+nx]:
                        visited[dy+ny][dx+nx] = True
                        q.append((dy+ny, dx+nx))

    return visited


f = g[0][0]
if g[-1][-1] != f:
    print("DEAD")
    exit()

visited = bfs(0, 0, [[False] * m for _ in range(n)])

if visited[-1][-1]:
    print("ALIVE")
else:
    print("DEAD")
