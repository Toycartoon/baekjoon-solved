r, c, zr, zc = map(int, input().split())
g = [[*input()] for _ in range(r)]

for y in range(r):
    for i in range(zr):
        for x in range(c):
            print(g[y][x] * zc, end="")
        print()
