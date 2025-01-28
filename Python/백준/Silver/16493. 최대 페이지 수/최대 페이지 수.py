n, m = map(int, input().split())

dp = [0 for _ in range(n + 1)]

for _ in range(m):
    day, page = map(int, input().split())
    for i in range(n, -1, -1):
        dp[i] = max(dp[i], dp[i-day] + page if i-day >= 0 else 0)


print(dp[-1])
