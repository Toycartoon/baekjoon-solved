n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort(reverse=True)
ans = 0
for i in range(m):
    if len(a)-i < 1:
        break

    if a[i] < 0:
        break
    else:
        ans += a[i]
        a.pop()

print(ans)
