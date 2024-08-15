from math import inf
import heapq
import sys

input = sys.stdin.readline


def dijkstra(x, y, distance):
    distance[y][x] = 0
    heapq.heappush(q, (0, x, y))

    pos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while q:
        dist, dx, dy = heapq.heappop(q)

        if distance[dy][dx] < dist:
            continue

        distance[dy][dx] = dist
        for _x, _y in pos:
            if 0 <= dy + _y < 501 and 0 <= dx + _x < 501:
                cost = dist + g[dy + _y][dx + _x]
                if cost < distance[dy + _y][dx + _x]:
                    distance[dy + _y][dx + _x] = cost
                    heapq.heappush(q, (cost, dx + _x, dy + _y))

    return distance


g = [[0 for __ in range(501)] for _ in range(501)]
visited = [[inf] * 501 for _ in range(501)]
q = []

n = int(input())
for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(min(y1, y2), max(y1, y2)+1):
        for x in range(min(x1, x2), max(x1, x2)+1):
            g[y][x] = 1


m = int(input())
for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(min(y1, y2), max(y1, y2)+1):
        for x in range(min(x1, x2), max(x1, x2)+1):
            g[y][x] = inf


ans = dijkstra(0, 0, visited)
if ans[500][500] == inf:
    print(-1)
else:
    print(ans[500][500])
