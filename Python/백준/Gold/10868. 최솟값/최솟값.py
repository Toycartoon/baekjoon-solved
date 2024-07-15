import sys
from math import inf

input = sys.stdin.readline

n, m = map(int, input().split())
tree = [inf for _ in range(n * 2)]


def query(tree, i, j):
    ans = inf

    i += len(tree) // 2 - 1
    j += len(tree) // 2 - 1

    while i <= j:
        if i % 2 == 1:
            ans = min(tree[i], ans)
            i += 1
        if j % 2 == 0:
            ans = min(tree[j], ans)
            j -= 1

        i //= 2
        j //= 2
        
    return ans


for i in range(n):
    tree[n + i] = int(input())

n = len(tree) // 2
for i in range(n-1, 0, -1):
    tree[i] = min(tree[i * 2], tree[i * 2 + 1])


for i in range(m):
    a, b = map(int, input().split())

    print(query(tree, a, b))
