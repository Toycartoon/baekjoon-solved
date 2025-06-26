n = int(input())
k = int(input())
a = list(map(int, input().split()))

ans = 0
for i in a:
    ans += max(0, i ** k)

print(ans)
