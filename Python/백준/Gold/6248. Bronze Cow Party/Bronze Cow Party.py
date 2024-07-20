from math import inf
import heapq

n, m, x = map(int, input().split())
g = [[] for _ in range(n)]
distance = [inf for _ in range(n)]

q = []

for i in range(m):
    a, b, t = map(int, input().split())

    g[a-1].append((t, b-1))
    g[b-1].append((t, a-1))


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


ans = dijkstra(x-1)
print(max(ans) * 2)
