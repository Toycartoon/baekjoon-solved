import sys

input = sys.stdin.readline

n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]

for k in range(int(input())):
    i, j, x, y = map(int, input().split())

    s = 0
    for a in range(i-1, x):
        for b in range(j-1, y):
            s += g[a][b]


    print(s)
