n = int(input())
a = list(map(int, input().split()))
dp = [a[i] for i in range(n)]

for i in range(n):
    k = []
    for j in range(i):
        if a[j] < a[i]:
            k.append(dp[j])

    dp[i] += max(k) if len(k) != 0 else 0

print(max(dp))

