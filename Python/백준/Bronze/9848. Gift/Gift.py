n, k = map(int, input().split())
t = int(input())
ans = 0
for i in range(n-1):
    s = int(input())
    if t - s >= k:
        ans += 1
    t = s

print(ans)
