dp = [0 for _ in range(1000001)]
dp[0] = 1
dp[1] = 2
dp[2] = 4

for i in range(3, len(dp)):
    dp[i] = (dp[i-3] + dp[i-2] + dp[i-1]) % 1000000009
    

for t in range(int(input())):
    print(dp[int(input())-1])
