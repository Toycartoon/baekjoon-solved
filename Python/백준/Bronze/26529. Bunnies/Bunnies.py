import sys


input = sys.stdin.readline

dp = [1] * 46
for i in range(2, 46):
    dp[i] = dp[i-1] + dp[i-2]


for i in range(int(input())):
    print(dp[int(input())])
