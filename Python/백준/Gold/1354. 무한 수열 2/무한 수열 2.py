import sys

sys.setrecursionlimit(10 ** 6)

n, p, q, x, y = map(int, input().split())

m = {0: 1}
def seq(n, p, q, x, y):
    global m

    if n <= 0:
        return m[0]
    if n in m:
        return m[n]
    v = seq(n // p - x, p, q, x, y) + seq(n // q - y, p, q, x, y)
    m[n] = v
    return m[n]

print(seq(n, p, q, x, y))