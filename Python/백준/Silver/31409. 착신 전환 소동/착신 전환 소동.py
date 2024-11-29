n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    if a[i] == i+1:
        ans += 1
        a[i] = 1 if a[i] != 1 else 2

print(ans)
print(*a)