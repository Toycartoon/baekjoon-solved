import heapq
import sys
from math import inf

v, e = map(int, input().split())
k = int(input())
g = [[] for _ in range(v)]
distance = [inf for _ in range(v)]
q = []


def dijkstra(s):
    distance[s] = 0
    heapq.heappush(q, (0, s))

    while q:
        dist, node = heapq.heappop(q)

        if distance[node] < dist:
            continue

        for i in g[node]:
            cost = dist + i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))


for _ in range(e):
    a, b, w = map(int, sys.stdin.readline().split())

    g[a - 1].append((w, b - 1))

dijkstra(k - 1)
for i in distance:
    print(str(i).upper())