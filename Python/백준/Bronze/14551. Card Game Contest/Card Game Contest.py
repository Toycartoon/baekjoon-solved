n, m = map(int, input().split())
ans = 1
for a in range(n):
    x = int(input())

    ans *= x if x != 0 else 1
    ans %= m

print(ans % m)