h = int(input())
dp = [0 for _ in range(h+1)]
dp[0] = 1

for i in range(1, h+1):
    if i % 2 == 0:
        dp[i] = dp[i-1] * 2 + 1
    else:
        dp[i] = dp[i-1] * 2 - 1

print(dp[h])
