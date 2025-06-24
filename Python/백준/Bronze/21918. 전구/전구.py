n, m = map(int, input().split())
ans = list(map(int, input().split()))

for _ in range(m):
    a, l, r = map(int, input().split())

    if a == 1:
        ans[l-1] = r
    elif a == 2:
        for i in range(l-1, r):
            ans[i] = int(not ans[i])
    elif a == 3:
        for i in range(l-1, r):
            ans[i] = 0
    elif a == 4:
        for i in range(l-1, r):
            ans[i] = 1

print(*ans)
