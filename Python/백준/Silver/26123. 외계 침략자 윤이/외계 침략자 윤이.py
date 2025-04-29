n, d = map(int, input().split())
h = list(map(int, input().split()))

ans = 0
x = max(0, max(h) - d)

for i in h:
    if i > x:
        ans += i-x

print(ans)
