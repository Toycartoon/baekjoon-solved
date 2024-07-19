import sys

input = sys.stdin.readline

n, m = map(int, input().split())
tree = [0 for _ in range(n)]

a = list(map(int, input().split()))
tree.extend(a)


def query(tree, i, j):
    ans = 0

    i += len(tree) // 2 - 1
    j += len(tree) // 2 - 1

    while i <= j:
        if i % 2 == 1:
            ans = max(ans, tree[i])
            i += 1
        if j % 2 == 0:
            ans = max(ans, tree[j])
            j -= 1

        i //= 2
        j //= 2

    return ans


n = len(tree) // 2
for i in range(n-1, 0, -1):
    tree[i] = max(tree[i * 2], tree[i * 2 + 1])

l = []
for i in range(m, n - m + 2):
    l.append(query(tree, i - m + 1, i + m - 1))


print(*l)
