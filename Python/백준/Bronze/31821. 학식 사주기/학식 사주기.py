n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

ans = 0
for _ in range(int(input())):
    ans += a[int(input())-1]

print(ans)
