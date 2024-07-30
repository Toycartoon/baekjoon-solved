# Special Thanks : jshyun912
n = int(input())
dp = [[0] * 15 for _ in range(1516)]

dp[0][0] = 1    # 자릿수가 0일 때, 15로 나눈 나머지가 0인 수가 하나 있음

for i in range(n):       # 자릿수
    for j in range(15):     # 나머지
        dp[i + 1][(j * 10 + 1) % 15] = (dp[i][j] + dp[i + 1][(j * 10 + 1) % 15]) % 1000000007
        dp[i + 1][(j * 10 + 5) % 15] = (dp[i][j] + dp[i + 1][(j * 10 + 5) % 15]) % 1000000007

print(dp[n][0])
