import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, r, q = map(int, input().split())
t = [[] for _ in range(n + 1)]
dp = [0 for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for i in range(n-1):
    u, v = map(int, input().split())
    t[u].append(v)
    t[v].append(u)


def dfs(x):
    visited[x] = True
    s = 1

    for i in t[x]:
        if not visited[i]:
            s += dfs(i)

    dp[x] = s
    return dp[x]


dfs(r)
for i in range(q):
    u = int(input())
    print(dp[u])
