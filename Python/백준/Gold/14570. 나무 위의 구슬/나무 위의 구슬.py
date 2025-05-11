import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

n = int(input())
t = [[] for _ in range(n+1)]

def dfs(n, x):
    if len(t[n]) == 0:
        return n
    elif len(t[n]) == 1:
        return dfs(t[n][0], x)
    else:
        if x % 2 == 0:
            return dfs(t[n][1], x // 2)
        else:
            return dfs(t[n][0], (x + 1) // 2)


for i in range(n):
    u, v = map(int, input().split())

    t[i+1].append(u) if u != -1 else 0
    t[i+1].append(v) if v != -1 else 0

k = int(input())
print(dfs(1, k))
