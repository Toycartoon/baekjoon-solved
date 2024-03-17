# Floyd-Warshall Algorithm vs toycartoon
from math import inf

n = int(input())
m = int(input())
g = [[inf] * (n + 1) for _ in range(n+1)]

for i in range(n+1):
    for j in range(n+1):
        if i == j:
            g[i][j] = 0


def floyd_warshall():
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if g[i][j] > g[i][k] + g[k][j]:
                    g[i][j] = g[i][k] + g[k][j]


for i in range(m):
    a, b, c = map(int, input().split())

    g[a][b] = min(g[a][b], c)


floyd_warshall()
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if g[i][j] == inf:
            print(0, end=" ")
        else:
            print(g[i][j], end=" ")
    print()
