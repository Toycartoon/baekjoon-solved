# Bellman-Ford Algorithm vs toycartoon
from math import inf


n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
distance = [inf for _ in range(n+1)]


def bellman_ford(start):
    distance[start] = 0
    for _ in range(n-1):
        for p_node in range(n+1):
            for n_node in g[p_node]:
                if distance[n_node[1]] > distance[p_node] + n_node[0]:
                    distance[n_node[1]] = distance[p_node] + n_node[0]

    for p_node in range(n+1):
        for n_node in g[p_node]:
            if distance[n_node[1]] > distance[p_node] + n_node[0]:
                return -1


for i in range(m):
    a, b, c = map(int, input().split())

    g[a].append((c, b))


ans = bellman_ford(1)
if ans == -1:
    print(-1)
else:
    for i in range(2, n+1):
        print(distance[i] if distance[i] != inf else -1)