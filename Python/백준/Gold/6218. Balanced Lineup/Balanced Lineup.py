import sys
from math import inf

input = sys.stdin.readline

n, q = map(int, input().split())
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
            min_l = [tree[i][0], ans[0]]
            max_l = [tree[i][1], ans[1]]

            min_l.sort()
            max_l.sort(reverse=True)

            ans = (min_l[0], max_l[0])
            i += 1
        if j % 2 == 0:
            min_l = [tree[j][0], ans[0]]
            max_l = [tree[j][1], ans[1]]

            min_l.sort()
            max_l.sort(reverse=True)

            ans = (min_l[0], max_l[0])
            j -= 1

        i //= 2
        j //= 2

    return ans


n = len(tree) // 2
for i in range(n-1, 0, -1):
    min_l = [tree[i * 2][0], tree[i * 2 + 1][0]]
    max_l = [tree[i * 2][1], tree[i * 2 + 1][1]]

    min_l.sort()
    max_l.sort(reverse=True)

    tree[i] = (min_l[0], max_l[0])


for i in range(q):
    a, b = map(int, input().split())

    print(abs(query(tree, a, b)[0] - query(tree, a, b)[1]))
