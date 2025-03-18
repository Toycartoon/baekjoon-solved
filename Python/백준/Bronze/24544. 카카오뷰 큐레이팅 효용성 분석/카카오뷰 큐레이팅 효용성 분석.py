n = int(input())
a = list(map(int, input().split()))
s = list(map(int, input().split()))

ans = 0
print(sum(a))

for i in range(n):
    if s[i] == 0:
        ans += a[i]

print(ans)
