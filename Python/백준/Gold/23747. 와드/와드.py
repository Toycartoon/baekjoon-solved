import sys
from collections import deque


input = sys.stdin.readline

r, c = map(int, input().split())
g = [[*input()] for _ in range(r)]
visited = [["#"] * c for _ in range(r)]

hr, hc = map(int, input().split())
hr -= 1
hc -= 1
s = input()


def bfs(_x, _y, color):
    q = deque()
    q.append((_x, _y))

    visited[_y][_x] = "."
    pos = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while q:
        x, y = q.popleft()
        for dx, dy in pos:
            if 0 <= x + dx < c and 0 <= y + dy < r:
                if g[y+dy][x+dx] == color and visited[y+dy][x+dx] == "#":
                    visited[y+dy][x+dx] = "."
                    q.append((x+dx, y+dy))


for i in range(len(s)):
    if s[i] == "U":
        hr -= 1
    elif s[i] == "D":
        hr += 1
    elif s[i] == "L":
        hc -= 1
    elif s[i] == "R":
        hc += 1
    elif s[i] == "W":
        bfs(hc, hr, g[hr][hc])

    if i == len(s) - 1:
        visited[hr][hc] = "."

        if 0 <= hr - 1:
            visited[hr-1][hc] = "."
        if hr + 1 < r:
            visited[hr+1][hc] = "."
        if 0 <= hc - 1:
            visited[hr][hc-1] = "."
        if hc + 1 < c:
            visited[hr][hc+1] = "."


for i in visited:
    print("".join(i))
