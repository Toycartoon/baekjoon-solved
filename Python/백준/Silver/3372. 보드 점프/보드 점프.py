n = int(input())
dp = [[0 for _ in range(n)] for _ in range(n)]
g = [list(map(int, input().split())) for _ in range(n)]

dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if g[i][j] == 0:
            continue

        if i + g[i][j] < n:
            dp[i+g[i][j]][j] += dp[i][j]
        if j + g[i][j] < n:
            dp[i][j+g[i][j]] += dp[i][j]


print(dp[-1][-1])
