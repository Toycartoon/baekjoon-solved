dp = [[0, 0, 0] for _ in range(100001)]

dp[0][0] = 1
dp[1][1] = 1
dp[2] = [1, 1, 1]
for i in range(3, len(dp)):
    dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % 1000000009
    dp[i][1] = (dp[i-2][2] + dp[i-2][0]) % 1000000009
    dp[i][2] = (dp[i-3][1] + dp[i-3][0]) % 1000000009


for t in range(int(input())):
    n = int(input())
    print(sum(dp[n-1]) % 1000000009)
