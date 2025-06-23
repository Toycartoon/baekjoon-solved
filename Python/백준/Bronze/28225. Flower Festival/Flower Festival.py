n, f = map(int, input().split())

ans = []
for i in range(n):
    x, v = map(int, input().split())
    ans.append(((f-x) / v, i+1))

ans.sort()
print(ans[0][1])
