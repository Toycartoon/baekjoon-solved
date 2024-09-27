code2 = 0
dp = [1] * 41
n = int(input())

for i in range(2, n):
    dp[i] = dp[i-1] + dp[i-2]
    code2 += 1


print(dp[n-1], code2)
