n, m = map(int, input().split())
a = list(map(int, input().split()))

ans = 1
for i in a:
    ans *= i % m
    ans %= m

print(ans)
