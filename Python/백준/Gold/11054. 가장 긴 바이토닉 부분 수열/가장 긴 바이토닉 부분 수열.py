n = int(input())
a = list(map(int, input().split()))

dp1 = [0 for _ in range(n)]
for i in range(n):
    dp1[i] = 1
    for j in range(i):
        if a[j] < a[i]:
            dp1[i] = max(dp1[i], dp1[j] + 1)


dp2 = [0 for _ in range(n)]
for i in range(n-1, -1, -1):
    dp2[i] = 1
    for j in range(n-1, i-1, -1):
        if a[j] < a[i]:
            dp2[i] = max(dp2[i], dp2[j] + 1)

ans = [0 for _ in range(n)]
for i in range(n):
    ans[i] = (dp1[i] + dp2[i] - 1)

print(max(ans))
