n, p, q = map(int, input().split())

m = {0: 1}
def seq(n, p, q):
    global m

    if n in m:
        return m[n]
    n1 = seq(n // p, p, q)
    n2 = seq(n // q, p, q)
    m[n] = n1 + n2
    return m[n]

print(seq(n, p, q))