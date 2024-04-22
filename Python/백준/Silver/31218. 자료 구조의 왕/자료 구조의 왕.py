import sys

input = sys.stdin.readline

n, m, q = map(int, input().split())
g = [[0] * n for _ in range(m)]

lg = n * m
for i in range(q):
    c, *l = map(int, input().split())

    if c == 1:
        dy = l[0]
        dx = l[1]
        y = l[2] - 1
        x = l[3] - 1
        while 0 <= y <= n-1 and 0 <= x <= m-1:
            if g[y][x] == 1:
                break
            else:
                g[y][x] = 1
                lg -= 1
                y += dy
                x += dx
    elif c == 2:
        y = l[0] - 1
        x = l[1] - 1
        print(g[y][x])
    elif c == 3:
       print(lg)
