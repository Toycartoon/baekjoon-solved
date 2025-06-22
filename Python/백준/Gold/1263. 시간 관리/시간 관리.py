n = int(input())
g = []
for i in range(n):
    t, s = map(int, input().split())
    g.append([t, s])

g.sort(key=lambda x: -x[1])
for i in range(1, n):
    g[i][1] = min(g[i][1], g[i-1][1] - g[i-1][0])

print(max(-1, g[-1][1] - g[-1][0]))
