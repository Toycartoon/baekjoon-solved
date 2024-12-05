n = int(input())
ans = 0

for a in range(-n, n+1):
    if a == 0:
        ans += (2 * n + 1) ** 2
        continue
    for b in range(-n, n+1):
        c = 1 - a - b
        if -n <= c <= n:
            ans += 1

print(ans)
