n = int(input())
l = list(map(int, input().split()))

ans = 0
x = l.index(max(l))
for i in range(x):
    ans += l[x] + l[i]

for i in range(x+1, n):
    ans += l[x] + l[i]


print(ans)
