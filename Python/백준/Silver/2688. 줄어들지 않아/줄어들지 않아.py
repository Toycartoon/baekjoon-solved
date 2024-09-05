dp = [[0 for _ in range(10)] for __ in range(65)]
for i in range(10):
    dp[1][i] = 1

for i in range(2, 65):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][:j+1])

for t in range(int(input())):
    print(sum(dp[int(input())]))
