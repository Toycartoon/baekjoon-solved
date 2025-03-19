n = int(input())

ans = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(j + 2, n+1):
            if i + j + k != n or i % 2 == 1:
                continue
            ans += 1

print(ans)
