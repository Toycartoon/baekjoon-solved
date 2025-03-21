n, r, c = map(int, input().split())
g = [["." for _ in range(n)] for __ in range(n)]

g[r-1][c-1] = "v"
if (r % 2 == 0 and c % 2 == 0) or (r % 2 == 1 and c % 2 == 1):
    for y in range(0, n, 2):
        for x in range(0, n, 2):
            g[y][x] = "v"

    for y in range(1, n, 2):
        for x in range(1, n, 2):
            g[y][x] = "v"
else:
    for y in range(0, n, 2):
        for x in range(1, n, 2):
            g[y][x] = "v"

    for y in range(1, n, 2):
        for x in range(0, n, 2):
            g[y][x] = "v"

for i in g:
    print("".join(i))
