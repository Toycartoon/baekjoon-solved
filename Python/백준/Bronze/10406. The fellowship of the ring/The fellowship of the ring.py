w, n, p = map(int, input().split())
h = list(map(int, input().split()))

ans = 0
for i in h:
    if w <= i <= n:
        ans += 1

print(ans)
