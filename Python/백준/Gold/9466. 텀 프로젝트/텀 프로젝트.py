import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(i):
    global ans

    visited[i] = True
    cycle.append(i)
    i = l[i]

    if visited[i]:
        if i in cycle:
            ans += len(cycle[cycle.index(i):])
    else:
        dfs(i)


for t in range(int(input())):
    n = int(input())
    l = [0] + list(map(int, input().split()))

    ans = 0
    visited = [False] * (n + 1)
    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(n - ans)
