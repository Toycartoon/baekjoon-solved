n, m = map(int, input().split())
k = list(map(int, input().split()))

ans = 0
for i in range(2, n+1):
    for x in k:
        if i % x == 0:
            ans += i
            break

print(ans)
