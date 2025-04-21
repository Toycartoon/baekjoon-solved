n, k = map(int, input().split())
l = []
for i in range(101):
    x = bin(i)
    l.extend([*x[2:]])

i = 0
ans = []
while i < 5:
    ans.append(l[i*n+k-1])
    i += 1

print(*ans)
