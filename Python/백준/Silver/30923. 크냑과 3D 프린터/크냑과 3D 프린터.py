n = int(input())
h = list(map(int, input().split()))

ans = n * 2
for i in range(1, n):
    ans += abs(h[i-1] - h[i])

ans += h[0] + h[-1] + (sum(h) * 2)
print(ans)
