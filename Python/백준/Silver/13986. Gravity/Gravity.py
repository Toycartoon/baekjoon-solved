n, m = map(int, input().split())

g = [[*input()] for _ in range(n)]

for y in range(n-1, -1, -1):
    for x in range(m):
        if g[y][x] == "o":
            g[y][x] = "."
            for i in range(y, n):
                if i == n-1:
                    g[i][x] = "o"
                elif g[i+1][x] == "#" or g[i+1][x] == "o":
                    g[i][x] = "o"
                    break


for i in g:
    print("".join(i))
