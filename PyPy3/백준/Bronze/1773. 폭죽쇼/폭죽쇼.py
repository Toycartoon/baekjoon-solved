n, c = map(int, input().split())
ans = [False for _ in range(c+1)]

x = []
for i in range(n):
    x.append(int(input()))

for i in x:
    for k in range(i, c+1, i):
        ans[k] = True

print(ans.count(True))
