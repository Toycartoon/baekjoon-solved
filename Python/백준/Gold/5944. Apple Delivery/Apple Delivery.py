import sys
import heapq
from math import inf


input = sys.stdin.readline

c, p, pb, pa1, pa2 = map(int, input().split())
g = [[] for _ in range(p)]
q = []


def dijkstra(s, e, distance):
    distance[s] = 0
    heapq.heappush(q, (0, s))

    while q:
        dist, node = heapq.heappop(q)

        if distance[node] < dist:
            continue

        distance[node] = dist
        for i in g[node]:
            cost = dist + i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                if i[1] != e:
                    heapq.heappush(q, (cost, i[1]))

    return distance


for i in range(c):
    p1, p2, d = map(int, input().split())

    g[p1-1].append((d, p2-1))
    g[p2-1].append((d, p1-1))


v1, v2 = 0, 0
distance = dijkstra(pb-1, pa1-1, [inf for _ in range(c)])
v1 += distance[pa1-1]
distance = dijkstra(pa1-1, pa2-1, [inf for _ in range(c)])
v1 += distance[pa2-1]

distance = dijkstra(pb-1, pa2-1, [inf for _ in range(c)])
v2 += distance[pa2-1]
distance = dijkstra(pa2-1, pa1-1, [inf for _ in range(c)])
v2 += distance[pa1-1]

print(min(v1, v2))
