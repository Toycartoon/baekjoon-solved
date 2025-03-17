n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

ans = 0
odd = []
for i in range(n):
    if a[i] % 2 == 0:
        ans += a[i]
    else:
        odd.append(a[i])

if len(odd) % 2 == 0:
    ans += sum(odd)
else:
    ans += sum(sorted(odd, reverse=True)[:-1])

print(ans)
