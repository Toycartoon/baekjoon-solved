from math import inf
import heapq, sys


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


gs = []
for t in range(int(input())):
    n, m = map(int, input().split())
    g = [[] for _ in range(n+1)]
    for i in range(m):
        v, w, x = map(int, input().split())

        if x >= 0:
            g[v].append((x, w))
        elif x < 0:
            g[v].append((gs[-x-1][0], w))
            g[w].append((gs[-x-1][1], v))

    distance1 = dijkstra(1, [inf for _ in range(n+1)])
    distance2 = dijkstra(2, [inf for _ in range(n+1)])
    gs.append((distance1[2], distance2[1]))

if gs[-1][0] > 10 ** 18:
    print(-1)
else:
    print(gs[-1][0])
