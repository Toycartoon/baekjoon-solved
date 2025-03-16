n, m, k = map(int, input().split())
g = [[*input()] for _ in range(n)]

for y in range(n):
    for i in range(k):
        for x in range(m):
            print(g[y][x] * k, end="")
        print()