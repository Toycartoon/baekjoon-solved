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


n, a, b = map(int, input().split())
g = [[] for _ in range(n+1)]
for i in range(n):
    k, *l = map(int, input().split())
    
    if k == 0:
        continue
        
    g[i+1].append((0, l[0]))
    for x in range(1, k):
        g[i+1].append((1, l[x]))


ans = dijkstra(a, [inf for _ in range(n+1)])
if ans[b] == inf:
    print(-1)
else:
    print(ans[b])
