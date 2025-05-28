import sys

input = sys.stdin.readline

n, x, k = map(int, input().split())
ans = [False for _ in range(n + 1)]

ans[x] = True
for i in range(k):
    a, b = map(int, input().split())
    ans[a], ans[b] = ans[b], ans[a]

print(ans.index(True))
