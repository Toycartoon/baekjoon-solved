import sys

input = sys.stdin.readline


def update(tree, i, val):
    i += len(tree) // 2 - 1
    tree[i] = (int(val % 2 == 0), int(val % 2 == 1))

    while i > 1:
        i //= 2
        tree[i] = (tree[i * 2][0] + tree[i * 2 + 1][0], tree[i * 2][1] + tree[i * 2 + 1][1])


def query(tree, i, j):
    ans = (0, 0)

    i += len(tree) // 2 - 1
    j += len(tree) // 2 - 1

    while i <= j:
        if i % 2 == 1:
            ans = (ans[0] + tree[i][0], ans[1] + tree[i][1])
            i += 1
        if j % 2 == 0:
            ans = (ans[0] + tree[j][0], ans[1] + tree[j][1])
            j -= 1

        i //= 2
        j //= 2

    return ans


n = int(input())
tree = [(0, 0) for x in range(n)]
a = list(map(int, input().split()))
for x in a:
    tree.append((int(x % 2 == 0), int(x % 2 == 1)))

n = len(tree) // 2
for i in range(n-1, 0, -1):
    tree[i] = (tree[i * 2][0] + tree[i * 2 + 1][0], tree[i * 2][1] + tree[i * 2 + 1][1])

m = int(input())
for x in range(m):
    q, l, r = map(int, input().split())

    if q == 1:
        update(tree, l, r)
    elif q == 2:
        print(query(tree, l, r)[0])
    elif q == 3:
        print(query(tree, l, r)[1])
