import heapq
import sys
from math import inf

n, e = map(int, input().split())
g = [[] for _ in range(n)]
distance = [inf for _ in range(n)]
q = []


def dijkstra(s, e):
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


for _ in range(e):
    a, b, dist = map(int, sys.stdin.readline().split())

    g[a - 1].append((dist, b - 1))
    g[b - 1].append((dist, a - 1))


v1, v2 = map(int, input().split())

a1 = 0
dijkstra(0, v1-1)
a1 += distance[v1-1]

distance = [inf for _ in range(n)]
dijkstra(v1-1, v2-1)
a1 += distance[v2-1]

distance = [inf for _ in range(n)]
dijkstra(v2-1, n-1)
a1 += distance[n-1]

distance = [inf for _ in range(n)]
a2 = 0
dijkstra(0, v2-1)
a2 += distance[v2-1]

distance = [inf for _ in range(n)]
dijkstra(v2-1, v1-1)
a2 += distance[v1-1]

distance = [inf for _ in range(n)]
dijkstra(v1-1, n-1)
a2 += distance[n-1]

if min(a1, a2) == inf:
    print(-1)
else:
    print(min(a1, a2))
