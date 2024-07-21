from math import inf
import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
g = [[] for _ in range(n)]
distance = [inf] * n
q = []


def dijkstra(s):
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


for i in range(m):
    a, b, c = map(int, input().split())

    g[a-1].append((c, b-1))
    g[b-1].append((c, a-1))


s, t = map(int, input().split())
distance = dijkstra(s-1)
print(distance[t-1])
