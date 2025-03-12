l = list(map(int, input().split()))

x = []
for i in l:
    if i % 2 == 1:
        x.append(i)

ans = 1
if len(x) == 0:
    for i in l:
        ans *= i
else:
    for i in x:
        ans *= i

print(ans)
