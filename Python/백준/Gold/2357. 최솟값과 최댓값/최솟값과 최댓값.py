import sys
from math import inf

input = sys.stdin.readline

n, m = map(int, input().split())
tree = [(inf, 0) for _ in range(n)]

for i in range(n):
    x = int(input())
    tree.append((x, x))


def query(tree, i, j):
    ans = (inf, 0)

    i += len(tree) // 2 - 1
    j += len(tree) // 2 - 1

    while i <= j:
        if i % 2 == 1:
            ans = (min(tree[i][0], ans[0]), max(tree[i][1], ans[1]))
            i += 1
        if j % 2 == 0:
            ans = (min(tree[j][0], ans[0]), max(tree[j][1], ans[1]))
            j -= 1

        i //= 2
        j //= 2

    return ans


n = len(tree) // 2
for i in range(n-1, 0, -1):
    tree[i] = (min(tree[i * 2][0], tree[i * 2 + 1][0]), max(tree[i * 2][1], tree[i * 2 + 1][1]))


for i in range(m):
    a, b = map(int, input().split())

    print(*query(tree, a, b))
