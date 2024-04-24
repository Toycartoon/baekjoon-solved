m = {}
for i in range(1, 15):
    m[(0, i)] = i


def f(k, n):
    if (k, n) in m:
        return m[(k, n)]

    v1 = 0
    for i in range(1, n + 1):
        v1 += f(k - 1, i)
    m[(k, n)] = v1
    return m[(k, n)]


for _ in range(int(input())):
    k = int(input())
    n = int(input())

    print(f(k, n))
