from math import inf
import heapq

n, m = map(int, input().split())
g = [list(map(int, [*input()])) for _ in range(m)]
visited = [[inf] * n for _ in range(m)]

q = []


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
            if 0 <= dy + _y < m and 0 <= dx + _x < n:
                cost = dist + g[dy+_y][dx+_x]
                if cost < distance[dy+_y][dx+_x]:
                    distance[dy+_y][dx+_x] = cost
                    heapq.heappush(q, (cost, dx+_x, dy+_y))

    return distance


print(dijkstra(0, 0, visited)[-1][-1])
