ans = []
for n in range(int(input())):
    a, b, c = map(int, input().split())

    if a + b + c >= 512:
        ans.append(a + b + c)

ans.sort()
if len(ans) == 0:
    print(-1)
else:
    print(ans[0])
