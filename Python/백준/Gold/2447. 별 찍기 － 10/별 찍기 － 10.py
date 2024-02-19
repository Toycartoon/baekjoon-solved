def f(n, x, y):
    if n == 1:
        ans[x][y] = "*"
        return
    a = n // 3
    f(a, x, y)
    f(a, x, y + a)
    f(a, x, y + 2 * a)
    f(a, x + a, y)
    f(a, x + a, y + 2 * a)
    f(a, x + 2 * a, y)
    f(a, x + 2 * a, y + a)
    f(a, x + 2 * a, y + 2 * a)


n = int(input())
ans = [[" " for i in range(n)] for j in range(n)]

f(n, 0, 0)

for i in ans:
    print("".join(i))
