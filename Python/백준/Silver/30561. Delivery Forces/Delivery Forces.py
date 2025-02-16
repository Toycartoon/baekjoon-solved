n = int(input())
f = list(map(int, input().split()))

f.sort()
ans = 0
for i in range(n // 3, n, 2):
    ans += f[i]

print(ans)
