n = int(input())
g = [[0, i, [False for _ in range(n+1)]] for i in range(n+1)]

for i in range(n+1):
    g[i][2][i] = True

for i in range(n-1):
    u, v = map(int, input().split())
    g[u][2][v] = True
    g[v][2][u] = True

    g[u][0] += 1
    g[v][0] += 1

if n <= 4:
    print("013"[n-2])
    print(1)
    for i in range(1, n+1):
        for j in range(1, n+1):
            if not g[i][2][j]:
                print(i, j)
                g[i][2][j] = True
                g[j][2][i] = True
    exit()

g.sort(key=lambda x: -x[0])
print(n-g[0][0]-1)
print(2)
for i in range(1, n+1):
    if not g[0][2][i]:
        print(g[0][1], i)
