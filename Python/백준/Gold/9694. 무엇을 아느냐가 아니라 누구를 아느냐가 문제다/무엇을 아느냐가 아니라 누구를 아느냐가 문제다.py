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
                pre[i[1]] = node
                heapq.heappush(q, (cost, i[1]))

    return distance


for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    g = [[] for _ in range(m)]
    distance = [inf for _ in range(m)]
    pre = [-1 for _ in range(m)]


    for i in range(n):
        x, y, z = map(int, input().split())

        g[x].append((z, y))
        g[y].append((z, x))


    dist = dijkstra(0, distance)

    if dist[m-1] == inf:
        print(f"Case #{t}: -1")
        continue
    
    ptr = m-1
    output = []
    while pre[ptr] != -1:
        output.append(ptr)
        ptr = pre[ptr]


    output.append(0)
    print(f"Case #{t}:", *output[::-1])
