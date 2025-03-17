import sys

input = sys.stdin.readline

n, m = map(int, input().split())
ans = [0 for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    ans[a] += 1
    ans[b] += 1

for i in range(1, n+1):
    print(ans[i])
