ans = 0
n = int(input())
for i in range(n):
    h, b, k = map(int, input().split())
    ans += max(0, b - h) * k

print(ans)
