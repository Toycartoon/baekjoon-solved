import sys
import heapq
from math import inf


input = sys.stdin.readline

n, m, k = map(int, input().split())
g = [[] for _ in range(n)]
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


for _ in range(m):
    u, v, c = map(int, input().split())

    g[u-1].append((c, v-1))
    g[v-1].append((c, u-1))


e = list(map(int, input().split()))
a = []
d1 = dijkstra(0, n-1, [inf for _ in range(n)])
d2 = dijkstra(n-1, 0, [inf for _ in range(n)])
for i in range(n):
    if e[i] == -1:
        continue

    v1 = d1[i]
    v2 = d2[i]
    
    if v1 == inf or v2 == inf:
        continue

    a.append(v1 + (e[i] * (k - 1)) + v2)


if len(a) == 0:
    print(-1)
else:
    print(min(a))
