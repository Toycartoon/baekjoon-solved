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


for t in range(int(input())):
    n, d, c = map(int, input().split())
    g = [[] for _ in range(n+1)]
    for i in range(d):
        a, b, s = map(int, input().split())

        g[b].append((s, a))

    distance = dijkstra(c, [inf for _ in range(n+1)])
    ans = 0
    m = 0
    for i in distance:
        if i != inf:
            ans += 1
            if i > m:
                m = i

    print(ans, m)
