n = int(input())
g = [["*" for __ in range(n)] for _ in range(n)]

for y in range(1, n-1):
    for x in range(1, n-1):
        g[y][x] = " "

for i in range(n):
    g[i][i] = "*"

for i in range(n):
    g[n-i-1][i] = "*"


for i in g:
    print("".join(i))
