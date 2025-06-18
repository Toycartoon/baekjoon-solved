n = int(input())
g = []
for i in range(n):
    x, y = map(int, input().split())
    g.append((x, y))

ans = 0
for i in range(n):
    ans += abs(g[i][0] - g[i-1][0]) + abs(g[i][1] - g[i-1][1])

print(ans)
