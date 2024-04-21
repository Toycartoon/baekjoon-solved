from math import inf


def bellman_ford(start):
    distance[start] = 0
    for _ in range(n-1):
        for p_node in range(n+1):
            for n_node in g[p_node]:
                if distance[n_node[1]] > distance[p_node] + n_node[0]:
                    distance[n_node[1]] = distance[p_node] + n_node[0]

    for p_node in range(1, n+1):
        for n_node in g[p_node]:
            if distance[n_node[1]] > distance[p_node] + n_node[0]:
                return -1


for tc in range(int(input())):
    n, m, w = map(int, input().split())
    g = [[] for _ in range(n + 1)]
    distance = [inf for _ in range(n + 1)]

    for i in range(m):
        s, e, t = map(int, input().split())

        g[s].append((t, e))
        g[e].append((t, s))

    for i in range(w):
        s, e, t = map(int, input().split())
        g[s].append((-t, e))

    for i in range(1, n+1):
        g[0].append((0, i))

    ans = bellman_ford(0)
    if ans == -1:
        print("YES")
    else:
        print("NO")