# Special Thanks: po_rani a.k.a.jbh0224, jshyun912

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
tree = [0 for _ in range(n + 1)]

a = [0] + list(map(int, input().split())) + [0]
for i in range(len(a)-1):
    tree.append(int(abs(a[i] - a[i + 1]) % 4 != 2))
tree.append(0)


def update(tree, i, val):
    a[i] = val
    idx = len(tree) // 2 + i
    tree[idx] = int(abs(a[i] - a[i + 1]) % 4 != 2)

    while idx > 1:
        idx //= 2
        tree[idx] = min(tree[idx * 2], tree[idx * 2 + 1])

    idx = len(tree) // 2 + i - 1
    tree[idx] = int(abs(a[i] - a[i - 1]) % 4 != 2)

    while idx > 1:
        idx //= 2
        tree[idx] = min(tree[idx * 2], tree[idx * 2 + 1])


def query(tree, i, j):
    f = 1

    i += len(tree) // 2 - 1
    j += len(tree) // 2 - 1

    while i <= j and f:
        if i % 2 == 1:
            f = min(tree[i], f)
            i += 1
        if j % 2 == 0:
            f = min(tree[j], f)
            j -= 1

        i //= 2
        j //= 2

    return f


n = len(tree) // 2
for i in range(n-1, 0, -1):
    tree[i] = min(tree[i * 2], tree[i * 2 + 1])

for i in range(m):
    q, ai, bi = map(int, input().split())

    if q == 1:
        update(tree, ai, bi)
    elif q == 2:
        print(query(tree, ai+1, bi))
