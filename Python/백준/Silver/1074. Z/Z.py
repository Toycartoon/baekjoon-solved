import sys

sys.setrecursionlimit(10 ** 6)

n, r, c = map(int, input().split())


def f(n, r, c):
    if n == 0:
        return 0

    a = 2 ** (n - 1)
    if r < a and c < a:
        return f(n-1, r, c)
    elif r < a <= c:
        return (a ** 2) + f(n-1, r, c - a)
    elif r >= a > c:
        return 2 * (a ** 2) + f(n-1, r - a, c)
    elif r >= a <= c:
        return 3 * (a ** 2) + f(n-1, r - a, c - a)


print(f(n, r, c))
