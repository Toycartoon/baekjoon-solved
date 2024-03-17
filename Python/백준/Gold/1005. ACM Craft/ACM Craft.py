import sys
from collections import deque


input = sys.stdin.readline

for t in range(int(input())):
    n, k = map(int, input().split())
    degree = [0] * (n + 1)
    g = [[] for _ in range(n+1)]
    td = list(map(int, input().split()))

    d = deque()
    for _ in range(k):
        x, y = map(int, input().split())
        g[x].append(y)
        degree[y] += 1

    w = int(input())

    for i in range(1, n+1):
        if degree[i] == 0:
            d.append(i)


    ans = []
    while d:
        cur = d.popleft()
        ans.append(cur)
        for nxt in g[cur]:
            degree[nxt] -= 1
            if degree[nxt] == 0:
                d.append(nxt)


    dp = [-1 for _ in range(n+1)]
    for i in ans:
        if dp[i] == -1:
            dp[i] = td[i-1]

        for nxt in g[i]:
            dp[nxt] = max(dp[nxt], dp[i] + td[nxt-1])

    print(dp[w])