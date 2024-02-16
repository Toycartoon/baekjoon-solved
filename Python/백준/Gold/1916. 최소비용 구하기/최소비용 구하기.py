# dijkstra Algorithm vs toycartoon
import heapq
import sys
from math import inf

n = int(input())
m = int(input())
g = [[] for _ in range(n)]
distance = [inf for _ in range(n)]
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


for _ in range(m):
    a, b, dist = map(int, sys.stdin.readline().split())

    g[a - 1].append((dist, b - 1))

s, r = map(int, input().split())

dijkstra(s - 1)
print(distance[r - 1])