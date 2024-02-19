import sys

sys.setrecursionlimit(10 ** 6)

m = {}
back = {}


def make_one(n):
    global m
    global back

    if n == 1:
        return 0
    if n in m:
        return m[n]

    c = [n // 3 if n % 3 == 0 else n - 1, n // 2 if n % 2 == 0 else n - 1]

    val = []
    for v in c:
        val.append(make_one(v))

    i = min(range(len(val)), key=lambda i: val[i])
    back[n] = c[i]
    m[n] = min(val) + 1

    return m[n]


n = int(input())
if n == 1:
    print(0)
    print(1)
    exit()
make_one(n)
ans = [n]
while ans[-1] != 1:
    v = back[ans[-1]]
    ans.append(v)

print(m[n])
for i in ans:
    print(i, end=" ")
