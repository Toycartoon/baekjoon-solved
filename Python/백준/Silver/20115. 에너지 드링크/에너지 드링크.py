n = int(input())
x = list(map(int, input().split()))

x.sort(reverse=True)
ans = x[0]

for i in range(1, n):
    ans += x[i] / 2

print(ans)
