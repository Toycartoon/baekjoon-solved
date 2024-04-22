import sys, collections

sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
g = [input().split() for _ in range(n)]
visited = [[0] * m for _ in range(n)]
q = collections.deque()
pos = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def bfs(r):
    visited[r[1]][r[0]] = 0

    q.append(r)
    while len(q) != 0:
        x, y = q.popleft()
        for wx, wy in pos:
            if 0 <= x + wx < m and 0 <= y + wy < n:
                if visited[y+wy][x+wx] == 0 and g[y+wy][x+wx] == "1":
                    visited[y+wy][x+wx] = visited[y][x] + 1
                    q.append([x+wx, y+wy])


x, y = 0, 0
f = False
for i in range(n):
    for j in range(m):
        if f:
            break
        if g[i][j] == "2":
            y, x = i, j
            f = True


bfs([x, y])
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            if (i, j) != (y, x) and g[i][j] != "0":
                print(-1, end=" ")
            else:
                print(0, end=" ")
        else:
            print(visited[i][j], end=" ")
    print()