n = int(input())
dp = [[0 for _ in range(9)] for __ in range(n)]
for i in range(9):
    dp[0][i] = 1

for i in range(1, n):
    for x in range(9):
        temp = 0
        for v in range(x-2, x+3):
            if 0 > v or 8 < v:
                continue
            temp += (dp[i-1][v]) % 987654321

        dp[i][x] = temp

print(sum(dp[n-1]) % 987654321)
