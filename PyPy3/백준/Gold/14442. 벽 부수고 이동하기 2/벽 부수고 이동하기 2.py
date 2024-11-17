from collections import deque

input = iter(open(0).read().split('\n')).__next__

n, m, k = map(int, input().split())
g = [list(map(int, [*input().strip()])) for _ in range(n)]
visited = [[[0] * (k + 1) for i in range(m)] for _ in range(n)]

q = deque()
pos = [(0, 1), (1, 0), (0, -1), (-1, 0)]

q.append((0, 0, 0))
visited[0][0][0] = 1

ans = -1

while q:
    x, y, w = q.popleft()

    if x == m-1 and y == n-1:
        ans = visited[y][x][w]
        break

    for dx, dy in pos:
        if 0 <= x + dx < m and 0 <= y + dy < n:
            if g[y+dy][x+dx] == 0 and visited[y+dy][x+dx][w] == 0:
                visited[y+dy][x+dx][w] = visited[y][x][w] + 1
                q.append((x+dx, y+dy, w))
            elif g[y+dy][x+dx] == 1 and w < k and visited[y+dy][x+dx][w+1] == 0:
                visited[y+dy][x+dx][w + 1] = visited[y][x][w] + 1
                q.append((x+dx, y+dy, w + 1))

print(ans)
