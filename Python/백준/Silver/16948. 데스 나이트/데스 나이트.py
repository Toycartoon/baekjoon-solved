from collections import deque

q = deque()
n = int(input())
r1, c1, r2, c2 = map(int, input().split())
visited = [[-1 for _ in range(n)] for __ in range(n)]

def bfs(_x, _y):
    visited[_y][_x] = 0
    pos = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]
    q.append((_x, _y))

    while q:
        x, y = q.popleft()

        for dx, dy in pos:
            if 0 <= x + dx < n and 0 <= y + dy < n:
                if visited[y+dy][x+dx] == -1:
                    visited[y+dy][x+dx] = visited[y][x] + 1
                    q.append((x+dx, y+dy))


bfs(r1, c1)
print(visited[c2][r2])