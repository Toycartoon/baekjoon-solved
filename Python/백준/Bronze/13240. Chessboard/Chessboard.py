n, m = map(int, input().split())

ans = ["*.*.*.*.*.*", ".*.*.*.*.*"] * 5
for i in range(n):
    print(ans[i][:m])
