n, q = map(int, input().split())
d = list(map(int, input().split()))

dp1 = [0 for _ in range(n)]
dp2 = [0 for _ in range(n)]
for i in range(n):
    dp1[i] = 1
    for j in range(i):
        if d[j] < d[i]:
            dp1[i] = max(dp1[i], dp1[j] + 1)

for i in range(n-1, -1, -1):
    dp2[i] = 1
    for j in range(n-1, i-1, -1):
        if d[j] > d[i]:
            dp2[i] = max(dp2[i], dp2[j] + 1)

for _ in range(q):
    a = int(input())
    print(dp1[a-1] + dp2[a-1] - 1)
