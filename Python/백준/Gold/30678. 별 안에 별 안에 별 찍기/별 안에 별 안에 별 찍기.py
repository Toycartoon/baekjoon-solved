def f(n, x, y):
    if n == 1:
        ans[x][y] = "*"
        return
    a = n // 5
    f(a, x, y + 2 * a)
    f(a, x + a, y + 2 * a)
    f(a, x + 2 * a, y)
    f(a, x + 2 * a, y + a)
    f(a, x + 2 * a, y + 2 * a)
    f(a, x + 2 * a, y + 3 * a)
    f(a, x + 2 * a, y + 4 * a)
    f(a, x + 3 * a, y + a)
    f(a, x + 3 * a, y + 2 * a)
    f(a, x + 3 * a, y + 3 * a)
    f(a, x + 4 * a, y + a)
    f(a, x + 4 * a, y + 3 * a)


n = int(input())
ans = [[" " for i in range(5 ** n)] for j in range(5 ** n)]

f(5 ** n, 0, 0)

for i in ans:
    print("".join(i))
