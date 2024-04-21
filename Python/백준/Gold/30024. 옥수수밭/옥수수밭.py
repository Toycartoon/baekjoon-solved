import heapq, sys

input = sys.stdin.readline

n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

q = []
pos = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = [[False] * m for _ in range(n)]

for i in range(n):
    heapq.heappush(q, (-g[i][0], i+1, 1))
    heapq.heappush(q, (-g[i][-1], i+1, m))

for i in range(1, m-1):
    heapq.heappush(q, (-g[0][i], 1, i+1))
    heapq.heappush(q, (-g[-1][i], n, i+1))


def bfs(y, x):
    for dx, dy in pos:
        if 0 <= x-1+dx <= m-1 and 0 <= y-1+dy <= n-1:
            if not visited[y-1+dy][x-1+dx]:
                heapq.heappush(q, (-g[y-1+dy][x-1+dx], y+dy, x+dx))


a = 0
while a < k:
    p = heapq.heappop(q)
    if not visited[p[1]-1][p[2]-1]:
        visited[p[1]-1][p[2]-1] = True

        print(p[1], p[2])
        bfs(p[1], p[2])
        a += 1

