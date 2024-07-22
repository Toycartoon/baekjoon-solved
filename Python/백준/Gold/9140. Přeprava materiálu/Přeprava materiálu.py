from math import inf
import sys
import heapq

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


while True:
    n, m, s, c = map(int, input().split())

    if n == m == s == c == 0:
        break

    g = [[] for _ in range(n)]
    for i in range(m):
        a, b, v = map(int, input().split())

        g[a-1].append((v, b-1))

    ans = dijkstra(s-1, [inf] * n)
    print(ans[c-1])
