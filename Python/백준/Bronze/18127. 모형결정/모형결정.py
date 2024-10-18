a, b = map(int, input().split())
ans = 0
i = 1
for x in range(b+1):
    ans += i
    i += a-2

print(ans)