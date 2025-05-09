n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(m)] for __ in range(n)]

for y in range(n):
    for x in range(m):
        dp[y][x] = max(dp[y-1][x-1] if 0 <= x-1 and 0 <= y-1 else 0, dp[y-1][x] if 0 <= y-1 else 0,
                       dp[y][x-1] if 0 <= x-1 else 0) + g[y][x]

print(dp[-1][-1])
