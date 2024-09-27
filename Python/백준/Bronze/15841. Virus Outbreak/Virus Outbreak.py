dp = [0] * 491
dp[1] = 1
for i in range(2, 491):
    dp[i] = dp[i-1] + dp[i-2]


while True:
    n = int(input())

    if n == -1:
        break


    print(f"Hour {n}: {dp[n]} cow(s) affected")
