n = int(input())
x, y = map(int, input().split())

ans = 0
for _ in range(n-1):
    i, j = map(int, input().split())
    ans += abs(x - i) + abs(y - j)
    x, y = i, j

print(ans)
