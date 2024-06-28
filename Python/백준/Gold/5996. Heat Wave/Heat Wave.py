import sys
import heapq
from math import inf

input = sys.stdin.readline

t, c, ts, te = map(int, input().split())
g = [[] for _ in range(t+1)]
visited = [inf] * (t+1)
q = []

for i in range(c):
    r1i, r2i, ci = map(int, input().split())
    g[r1i].append((ci, r2i))
    g[r2i].append((ci, r1i))


def dijkstra(s, distance):
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
                heapq.heappush(q, (cost, i[1]))

    return distance


ans = dijkstra(ts, visited)
print(ans[te])
