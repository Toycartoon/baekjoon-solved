for t in range(int(input())):
    n = int(input())
    coin = list(map(int, input().split()))
    m = int(input())

    dp = [0 for _ in range(m + 1)]
    dp[0] = 1
    for i in range(n):
        for j in range(m+1-coin[i]):
            dp[j+coin[i]] += dp[j]

    print(dp[m])
