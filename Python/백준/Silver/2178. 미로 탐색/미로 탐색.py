import sys, collections

sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
g = [input() for _ in range(n)]
visited = [[0] * m for _ in range(n)]
q = collections.deque()
pos = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def bfs(r):
    visited[r[0]][r[1]] = 1

    q.append(r)
    while len(q) != 0:
        x, y = q.popleft()
        for wx, wy in pos:
            if 0 <= x + wx < m and 0 <= y + wy < n:
                if visited[y+wy][x+wx] == 0 and g[y+wy][x+wx] == "1":
                    visited[y+wy][wx+x] = visited[y][x] + 1
                    q.append([x+wx, y+wy])

bfs([0, 0])
print(visited[n-1][m-1])