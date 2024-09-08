n = int(input())
s = list(map(int, input().split()))

ans = (n - 1) * 180
for i in s:
    ans -= i * 2


print(ans)
