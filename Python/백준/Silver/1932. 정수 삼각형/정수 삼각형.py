import sys

sys.setrecursionlimit(10 ** 6)

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
memo = [[0] * i for i in range(1, n)]
def dp(depth, idx):
    if depth == n:
        return g[depth-1][idx]
    if memo[depth-1][idx] != 0:
        return memo[depth-1][idx]

    v1 = dp(depth+1, idx)
    v2 = dp(depth+1, idx+1) if idx < depth else 0

    memo[depth-1][idx] = g[depth-1][idx] + max(v1, v2)
    return memo[depth-1][idx]

print(dp(1, 0))
