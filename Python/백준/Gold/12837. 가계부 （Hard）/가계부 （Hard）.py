import sys

input = sys.stdin.readline

n, m = map(int, input().split())
tree = [0 for _ in range(n * 2)]

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


for i in range(m):
    q, p, x = map(int, input().split())

    if q == 1:
        update(tree, p, x)
    elif q == 2:
        print(query(tree, p, x))
