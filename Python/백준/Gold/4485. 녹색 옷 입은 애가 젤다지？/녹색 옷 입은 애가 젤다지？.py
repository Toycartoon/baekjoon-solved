from math import inf
import heapq
import sys

input = sys.stdin.readline


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


t = 0
while True:
    n = int(input())

    if n == 0:
        break

    g = [list(map(int, [*input().strip().split()])) for _ in range(n)]
    visited = [[inf] * n for _ in range(n)]
    q = []

    print(f"Problem {t+1}:", dijkstra(0, 0, visited)[-1][-1])
    t += 1
