import sys
from math import inf

input = sys.stdin.readline


def update(tree, i, j):
    i += len(tree) // 2 - 1
    j += len(tree) // 2 - 1
    tree[i], tree[j] = tree[j], tree[i]

    while i > 1:
        i //= 2
        tree[i] = (min(tree[i * 2][0], tree[i * 2 + 1][0]), tree[i * 2][1] + tree[i * 2 + 1][1])

    while j > 1:
        j //= 2
        tree[j] = (min(tree[j * 2][0], tree[j * 2 + 1][0]), tree[j * 2][1] + tree[j * 2 + 1][1])

def query(tree, i, j):
    ans = (inf, 0)

    i += len(tree) // 2 - 1
    j += len(tree) // 2 - 1

    while i <= j:
        if i % 2 == 1:
            ans = (min(tree[i][0], ans[0]), ans[1] + tree[i][1])
            i += 1
        if j % 2 == 0:
            ans = (min(tree[j][0], ans[0]), ans[1] + tree[j][1])
            j -= 1

        i //= 2
        j //= 2

    return ans


for t in range(int(input())):
    n, k = map(int, input().split())
    tree = [(inf, 0) for x in range(n)]
    for x in range(n):
        tree.append((x, x))

    n = len(tree) // 2
    for i in range(n-1, 0, -1):
        tree[i] = (min(tree[i * 2][0], tree[i * 2 + 1][0]), tree[i * 2][1] + tree[i * 2 + 1][1])


    for x in range(k):
        q, a, b = map(int, input().split())

        if q == 0:
            update(tree, a+1, b+1)
        elif q == 1:
            v = query(tree, a+1, b+1)

            if v[0] == a and v[1] == (b - a + 1) * (a + b) // 2:
                print("YES")
            else:
                print("NO")
