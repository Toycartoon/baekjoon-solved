from collections import deque
import sys

input = sys.stdin.readline


q = deque()
def bfs(_x, _y, _z):
    pos = [(0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0)]
    q.append((_x, _y, _z))
    visited[_z][_y][_x] = 0

    while q:
        x, y, z = q.popleft()

        for dx, dy, dz in pos:
            if 0 <= x+dx < c and 0 <= y+dy < r and 0 <= z+dz < l:
                if visited[z+dz][y+dy][x+dx] == -1 and g[z+dz][y+dy][x+dx] != "#":
                    visited[z+dz][y+dy][x+dx] = visited[z][y][x] + 1
                    q.append((x+dx, y+dy, z+dz))


while True:
    l, r, c = map(int, input().split())

    if l == r == c == 0:
        break

    g = [[] for _ in range(l)]
    i = 0
    for z in range(l * r + l):
        s = input().strip()
        if s != "":
            g[i].append([*s])
        else:
            i += 1

    visited = [[[-1 for _ in range(c)] for __ in range(r)] for ___ in range(l)]
    sx, sy, sz = -1, -1, -1
    ex, ey, ez = -1, -1, -1

    for z in range(l):
        for y in range(r):
            for x in range(c):
                if g[z][y][x] == "S":
                    sx, sy, sz = x, y, z
                elif g[z][y][x] == "E":
                    ex, ey, ez = x, y, z

    bfs(sx, sy, sz)
    ans = visited[ez][ey][ex]
    if ans == -1:
        print("Trapped!")
    else:
        print(f"Escaped in {ans} minute(s).")
