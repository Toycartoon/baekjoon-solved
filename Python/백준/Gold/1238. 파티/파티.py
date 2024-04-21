import heapq
import sys
from math import inf

n, m, x = map(int, input().split())
g = [[] for _ in range(n + 1)]
distance = [inf for _ in range(n + 1)]
q = []


def dijkstra(s, e):
    heapq.heappush(q, (0, s))

    while q:
        dist, node = heapq.heappop(q)

        if distance[node] < dist:
            continue

        for i in g[node]:
            cost = dist + i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                if i[1] != e:
                    heapq.heappush(q, (cost, i[1]))


for _ in range(m):
    a, b, dist = map(int, sys.stdin.readline().split())

    g[a].append((dist, b))


l = []
for i in range(1, n+1):
    if i == x:
        continue
    t = 0
    distance = [inf for _ in range(n + 1)]
    dijkstra(i, x)
    t += distance[x]

    distance = [inf for _ in range(n + 1)]
    dijkstra(x, i)
    t += distance[i]

    l.append(t)

print(max(l))
