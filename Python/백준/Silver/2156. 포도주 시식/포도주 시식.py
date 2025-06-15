import sys

input = sys.stdin.readline

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

dp = [[0, 0] for _ in range(n+1)]
dp[1][0] = a[0]
dp[1][1] = a[0]
for i in range(2, n+1):
    dp[i][0] = max(max(dp[:i-1], key=lambda x: x[0])[0], max(dp[:i-1], key=lambda x: x[1])[1]) + a[i-1]
    dp[i][1] = dp[i-1][0] + a[i-1]

print(max(max(dp, key=lambda x: x[0])[0], max(dp, key=lambda x: x[1])[1]))
