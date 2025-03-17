n, m = map(int, input().split())
a = list(map(int, input().split()))

w = [-1 for _ in range(100001)]
for _ in range(m):
    x, *t = input().split()

    i = 0
    for v in range(n):
        if t[v] == "O":
            i += a[v]

    w[int(x)] = i

print(w.index(max(w)), max(w))
