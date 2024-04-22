def f(n, x):
    if n == 1:
        ans[x] = "-"
        return
    a = n // 3
    f(a, x)
    f(a, x + 2 * a)


while True:
    try:
        n = int(input())
        ans = [" " for i in range(3 ** n)]

        f(3 ** n, 0)

        print("".join(ans))
    except EOFError:
        break