from math import inf
import heapq


def dijkstra(x, y, distance):
    distance[y][x] = g[y][x]
    heapq.heappush(q, (g[y][x], x, y))

    pos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while q:
        dist, dx, dy = heapq.heappop(q)

        if distance[dy][dx] < dist:
            continue

        distance[dy][dx] = dist
        for _x, _y in pos:
            if 0 <= dy + _y < n and 0 <= dx + _x < n:
                cost = dist + g[dy + _y][dx + _x]
                if cost < distance[dy + _y][dx + _x]:
                    distance[dy + _y][dx + _x] = cost
                    heapq.heappush(q, (cost, dx + _x, dy + _y))

    return distance


n = int(input())
g = [list(map(int, [*input()])) for _ in range(n)]
for y in range(n):
    for x in range(n):
        if g[y][x] == 1:
            g[y][x] = 0
        else:
            g[y][x] = 1
visited = [[inf] * n for _ in range(n)]
q = []

print(dijkstra(0, 0, visited)[-1][-1])
