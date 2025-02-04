import sys

input = sys.stdin.readline

r, c = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(r)]
ans = [[0 for _ in range(c)] for __ in range(r)]

for y in range(1, r-1):
    for x in range(1, c-1):
        if g[y][x] < g[y-1][x] and g[y][x] < g[y+1][x] and g[y][x] < g[y][x-1] and g[y][x] < g[y][x+1]:
            ans[y][x] = 1


for i in ans:
    print(*i)
