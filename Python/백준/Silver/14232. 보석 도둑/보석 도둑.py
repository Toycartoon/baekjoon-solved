k = int(input())

ans = []
for i in range(2, int(k ** 0.5) + 1):
    while k % i == 0:
        k //= i
        ans.append(i)

ans.append(k) if k != 1 else ""

print(len(ans))
print(*ans)
