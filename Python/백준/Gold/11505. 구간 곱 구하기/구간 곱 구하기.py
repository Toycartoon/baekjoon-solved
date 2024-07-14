import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
tree = [0 for _ in range(n * 2)]


def update(tree, i, val):
    i += len(tree) // 2 - 1
    tree[i] = val

    while i > 1:
        i //= 2
        tree[i] = tree[i * 2] * tree[i * 2 + 1] % 1000000007


def query(tree, i, j):
    ans = 1

    i += len(tree) // 2 - 1
    j += len(tree) // 2 - 1

    while i <= j:
        if i % 2 == 1:
            ans *= tree[i]
            i += 1
        if j % 2 == 0:
            ans *= tree[j]
            j -= 1

        i //= 2
        j //= 2
        ans %= 1000000007

    return ans % 1000000007


for i in range(n):
    tree[n + i] = int(input())

n = len(tree) // 2

for i in range(n-1, 0, -1):
    tree[i] = tree[i * 2] * tree[i * 2 + 1] % 1000000007


for i in range(m + k):
    a, b, c = map(int, input().split())

    if a == 1:
        update(tree, b, c)
    elif a == 2:
        print(query(tree, b, c))
