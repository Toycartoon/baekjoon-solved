from math import inf

n, m, r = map(int, input().split())
item = list(map(int, input().split()))
g = [[inf] * (n + 1) for _ in range(n+1)]

for i in range(n+1):
    g[i][i] = 0


def floyd_warshall():
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if g[i][j] > g[i][k] + g[k][j]:
                    g[i][j] = g[i][k] + g[k][j]


for i in range(r):
    a, b, c = map(int, input().split())

    g[a][b] = min(g[a][b], c)
    g[b][a] = min(g[b][a], c)


floyd_warshall()
e = []
for i in range(1, n + 1):
    v = 0
    for j in range(1, n + 1):
        if g[i][j] != inf:
            if g[i][j] <= m:
                v += item[j-1]

    e.append(v)

print(max(e))
