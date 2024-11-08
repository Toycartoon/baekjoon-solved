from math import trunc


h, y = map(int, input().split())
dp = [0 for _ in range(y+1)]

dp[0] = h
for i in range(1, y+1):
    dp[i] = max(trunc(dp[i-1] * 1.05), trunc(dp[i-3] * 1.2) if i >= 3 else 0, trunc(dp[i-5] * 1.35) if i >= 5 else 0)

print(dp[-1])
