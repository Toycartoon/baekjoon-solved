import sys
import heapq
from math import inf


input = sys.stdin.readline

n = int(input())
e = int(input())
t = int(input())
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


for i in range(int(input())):
    a, b, c = map(int, input().split())

    g[a-1].append((c, b-1))


ans = 0
for i in range(n):
    distance = dijkstra(i, e-1, [inf for _ in range(n)])

    if distance[e-1] <= t:
        ans += 1

print(ans)
