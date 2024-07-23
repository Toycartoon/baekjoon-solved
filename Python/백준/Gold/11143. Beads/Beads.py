import sys

input = sys.stdin.readline


def update(tree, i, val):
    i += len(tree) // 2 - 1
    tree[i] += val

    while i > 1:
        i //= 2
        tree[i] = tree[i * 2] + tree[i * 2 + 1]


def query(tree, i, j):
    ans = 0

    i += len(tree) // 2 - 1
    j += len(tree) // 2 - 1

    while i <= j:
        if i % 2 == 1:
            ans += tree[i]
            i += 1
        if j % 2 == 0:
            ans += tree[j]
            j -= 1

        i //= 2
        j //= 2

    return ans


for t in range(int(input())):
    n, p, q = map(int, input().split())
    tree = [0] * (n * 2)

    n = len(tree) // 2

    for i in range(n-1, 0, -1):
        tree[i] = tree[i * 2] + tree[i * 2 + 1]

    for i in range(p + q):
        a, b, c = input().split()

        if a == "P":
            update(tree, int(b), int(c))
        elif a == "Q":
            print(query(tree, int(b), int(c)))
