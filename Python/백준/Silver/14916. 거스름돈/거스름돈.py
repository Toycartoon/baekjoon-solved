import sys

sys.setrecursionlimit(10 ** 6)

m = {2: 1, 5: 1}


def check(n):
    if n < 2:
        return -1
    if n in m:
        return m[n]
    v1 = check(n - 2) + 1
    v2 = check(n - 5) + 1

    if v1 == 0 and v2 == 0:
        return -1
    if v1 == 0:
        m[n] = v2
    elif v2 == 0:
        m[n] = v1
    else:
        m[n] = min(v1, v2)

    return m[n]

print(check(int(input())))