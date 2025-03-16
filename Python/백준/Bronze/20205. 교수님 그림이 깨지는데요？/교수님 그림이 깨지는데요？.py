n, k = map(int, input().split())
g = [input().split() for _ in range(n)]

for y in range(n):
    for i in range(k):
        for x in range(n):
            print((g[y][x] + " ") * k, end="")
        print()