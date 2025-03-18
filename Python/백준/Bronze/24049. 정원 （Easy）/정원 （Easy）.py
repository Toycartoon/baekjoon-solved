import sys

input = sys.stdin.readline

n, m = map(int, input().split())
g = [[0 for _ in range(m+1)] for __ in range(n+1)]

i = list(map(int, input().split()))
j = list(map(int, input().split()))

for x in range(1, n+1):
    g[x][0] = i[x-1]

for x in range(1, m+1):
    g[0][x] = j[x-1]

for y in range(1, n+1):
    for x in range(1, m+1):
        if g[y-1][x] == g[y][x-1]:
            g[y][x] = 0
        else:
            g[y][x] = 1

print(g[n][m])
