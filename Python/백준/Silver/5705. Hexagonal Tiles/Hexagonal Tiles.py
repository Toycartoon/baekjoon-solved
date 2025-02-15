dp = [1 for _ in range(41)]
for i in range(2, 41):
    dp[i] = dp[i-1] + dp[i-2]


while True:
    n = int(input())

    if n == 0:
        break

    print(dp[n])
