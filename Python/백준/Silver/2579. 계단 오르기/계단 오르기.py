n = int(input())
s = [int(input()) for _ in range(n)]

m = {(0, False): s[0], (0, True): s[0]}


def c(i, st: bool):
    if i < 0:
        return 0
    if (i, st) in m:
        return m[(i, st)]

    v2 = c(i - 2, False)
    if st:
        m[(i, st)] = v2 + s[i]
        return m[(i, st)]
    v1 = c(i - 1, True)
    m[(i, st)] = max(v1, v2) + s[i]

    return m[(i, st)]

c(n - 1, False)
if (n - 1, True) not in m:
    print(m[(n - 1, False)])
elif (n - 1, False) not in m:
    print(m[(n - 1, True)])
else:
    print(max(m[(n - 1, True)], m[(n - 1, False)]))
