import heapq
import sys
from math import inf

input = sys.stdin.readline


q = []
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


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

g = [[] for _ in range(n + 2)]
for i in range(1, n+1):
    g[max(i - a[i-1], 0)].append((b[i-1], i))
    g[min(i + a[i-1], n+1)].append((b[i-1], i))

distance1 = dijkstra(0, [inf for _ in range(n+2)])
distance2 = dijkstra(n+1, [inf for _ in range(n+2)])

for i in range(1, n+1):
    print(min(distance1[i], distance2[i]), end=" ")
