from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
g = [list(map(int, [*input().strip()])) for _ in range(n)]
visited = [[[0, 0] for i in range(m)] for _ in range(n)]

q = deque()


def bfs(_x, _y):
    pos = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    q.append((_x, _y, 0))
    visited[_y][_x][0] = 1

    while q:
        x, y, w = q.popleft()

        if x == m-1 and y == n-1:
            return visited[y][x][w]

        for dx, dy in pos:
            if 0 <= x + dx < m and 0 <= y + dy < n:
                if g[y+dy][x+dx] == 0 and visited[y+dy][x+dx][w] == 0:
                    visited[y+dy][x+dx][w] = visited[y][x][w] + 1
                    q.append((x+dx, y+dy, w))
                elif g[y+dy][x+dx] == 1 and w == 0:
                    visited[y+dy][x+dx][w + 1] = visited[y][x][w] + 1
                    q.append((x+dx, y+dy, w + 1))

    return -1


print(bfs(0, 0))
