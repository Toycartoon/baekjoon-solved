n = int(input())
ans = 0
for a in range(1, n+1):
    for b in range(a, n+1):
        c = n - (a + b)
        if b > c:
            break
        if a + b > c:
            ans += 1

print(ans)
